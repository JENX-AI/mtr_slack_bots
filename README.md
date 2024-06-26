# MTR Slack Bots

This program contains LLM apps developed for integration with the Slack platform.

The apps include four chatbots using various large language models; a text-to-image generation model; and a custom model designed to introduce new members upon joining the MTR Slack channel.

## Contents

- [Directory structure](#directory-structure)
- [Models](#models)
- [Installation](#installation)
- [Operation](#operation)
- [Terms and conditions](#terms-and-conditions)

## Models

Source: [together.ai](https://docs.together.ai/docs/inference-models)

| Organization | Model Name            | Model String for API               | Context length | Type  |
| ------------ | --------------------- | ---------------------------------- | -------------- | ----- |
| 01.AI        | 01-ai Yi Chat (34B)   | zero-one-ai/Yi-34B-Chat            | 4096           | Chat  |
| Meta         | LLaMA-2 Chat (13B)    | meta-llama/Llama-2-13b-chat-hf     | 4096           | Chat  |
| mistralai    | Mistral (7B) Instruct | mistralai/Mistral-7B-Instruct-v0.1 | 8192           | Chat  |
| Stanford     | Alpaca (7B)           | togethercomputer/alpaca-7b         | 2048           | Chat  |
| Stability AI | Stable Diffusion 2.1  | stabilityai/stable-diffusion-2-1   | N/A            | Image |

\*The Intro-Bot app makes use of the Llama-2-13b-chat-hf model.

## Directory structure

The directory is organised as indicated in the table below, with separate sub-directories for each of the four chat models, the image model, and introductions model. The model directories contain numerous files that form the source code for each app, and that are not displayed here.

| Parent directory     | `mtr_slack_bots` contents | `slack_bots` contents      |
| -------------------- | ------------------------- | -------------------------- |
| `mtr_slack_bots` `/` | `install.sh`              |                            |
|                      | `run_all.sh`              |                            |
|                      | `slack_bots` `/`          | `alpaca-7b`                |
|                      |                           | `Llama-2-13b-chat-hf`      |
|                      |                           | `Mistral-7B-Instruct-v0.1` |
|                      |                           | `Yi-34B-Chat`              |
|                      |                           | `Image-Bot`                |
|                      |                           | `Intro-Bot`                |

## Installation

To install the program, load the entire directory structure contained within `mtr_slack_bots` onto the relevant cloud compute instance or local drive.

Navigate inside the main `mtr_slack_bots` directory and run the `install.sh` file:

```console
~$ cd mtr_slack_bots
~/mtr_slack_bots$ chmod +x install.sh
~/mtr_slack_bots$ ./install.sh
```

## Operation

Set up the relevant Slack apps in the desired Slack workspace as per the separate instructions provided (see slack_app_setup.pdf for detailed step-by-step instructions).

Create `.env` files within each bot's base directory (so on the same level as where you will find each pyproject.toml file) with their respective Slack app token, Slack bot token, and Together.ai API key inserted as referenced in the above PDF document.

### Run all bots

Navigate inside the main `mtr_slack_bots` directory and run the `install.sh` file:

```console
~$ cd mtr_slack_bots
~/mtr_slack_bots$ chmod +x run_all.sh
~/mtr_slack_bots$ ./run_all.sh
```

### Run one bot

Navigate inside the directory of the bot (e.g., `alpaca-7b`) and run the `run.sh` file:

```console
~$ cd mtr_slack_bots/slack_bots/alpaca-7b
~/alpaca-7b$ chmod +x run.sh
~/alpaca-7b$ ./run.sh
```

## Termination

To stop the bot(s), run:

```console
~$ ps aux | grep app.py
```

The process ID (PID) numbers for each service will be listed as the first number on each line.

Note the PID for the relevant process for the model to terminate, then run:

```console
~$ kill <PID>
```

## Terms and conditions

This project was developed between March and April 2024 on behalf of Gene Soo of MTR Corporation Limited by Joyce Chung, Nicholas Dykema and Elliott Steer ("the Authors").

The source code is provided to MTR Corporation Limited by the Authors free of charge, and may be distributed in accordance with the project license provided that the Authors are fairly credited for their work.

If in need of further information or support, please contact the Authors on:

- Joyce Chung, joycechungyt@gmail.com
- Nicholas Dykema, nicowork13@gmail.com
- Elliott Steer, essteer@pm.me
