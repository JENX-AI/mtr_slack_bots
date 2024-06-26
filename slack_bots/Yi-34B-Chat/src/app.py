# -*- coding: utf-8 -*-
import os, logging
from dotenv import load_dotenv
import slack_bolt
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

from utils.logger import get_logger
from utils.model_funcs import build_chain, add_chain_link, THREADS_DICT
# Credentials
load_dotenv()
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]

app = App(token=SLACK_BOT_TOKEN)
client = WebClient(SLACK_BOT_TOKEN)
logger = get_logger(__name__)

# ====================================
# Slack event listeners
# ====================================

@app.message(".*")
def message_handler(message: dict, say: slack_bolt.Say, logger: logging.Logger) -> None:
    """
    Handles messages to chatbot within Apps
    
    Parameters
    ----------
    message : dict
        message received from Slack user in Apps
    
    say : slack_bolt.Say
        sends message to Slack
    
    logger : logging.Logger
        logging object
    """
    try:
        # ID for channel message received from
        # Set thread timestamp as channel ID 
        try:
            channel_id = message["thread_ts"]
        except KeyError:
            channel_id = message["ts"]
        
        # If no chain exists for this channel, create new one
        if not channel_id in THREADS_DICT:
            build_chain(channel_id)
        
        # Store user_message and get bot response
        bot_message = add_chain_link(channel_id, message, loc="apps")
        
        # Send generated response back in a thread
        thread_timestamp = message["ts"]
        say(bot_message, thread_ts = thread_timestamp)
        
    except Exception as e:
        logger.error(f"Error: {e}")


@app.event(("app_mention"))
def handle_app_mention_events(body: dict, say: slack_bolt.Say, logger: logging.Logger) -> None:
    """
    Handles direct (@) messages to chatbot within Channels
    
    Parameters
    ----------
    body : dict
        message received from Slack user in Channels
    
    say : slack_bolt.Say
        sends message to Slack
    
    logger : logging.Logger
        logging object
    """
    try:
        # ID for channel message received from
        # Set thread timestamp as channel ID 
        try:
            channel_id = body["event"]["thread_ts"]
        except KeyError:
            channel_id = body["event"]["ts"]
        
        # If no chain exists for this channel, create new one
        if not channel_id in THREADS_DICT:
            build_chain(channel_id)
        
        # Store user_message and get bot response
        bot_message = add_chain_link(channel_id, body, loc="mentions")
    
        # Send generated response back in a thread
        thread_timestamp = body["event"]["ts"]
        say(bot_message, thread_ts = thread_timestamp)
    
    except Exception as e:
        logger.error(f"Error: {e}")


# ====================================
# Initialisation
# ====================================

if __name__ == "__main__":
    # Create an app-level token with connections:write scope
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
