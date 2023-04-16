import os
import sys
import random
import config
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from config import OWNER_ID
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

print("[KHUNI] Version Check is being Processed") 
#VERSION
deadlyversion = "v3.0.0"

print("[KHUNI] Booting sudolist") 
#SUDOERS
SUDOERS = config.SUDO_USER
SUDOERS.append(OWNER_ID) 

# OWNER COMMAND 

CHUT = config.CHUT
CHUT.append(OWNER_ID) 
# ECHO LIST

print("[KHUNI] Preparing ECHO cmd check") 

ECHOUSER = config.LUND
ECHOUSER.append(f"config.ECHOUSER") 
# CLIENTS

print("[KHUNI] Starting First SpamBot") 
BOT0 = TelegramClient('BOT0', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN)

print("[KHUNI] Starting Second SpamBot") 
BOT1 = TelegramClient('BOT1', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN2)

print("[KHUNI] Starting Third SpamBot") 
BOT2 = TelegramClient('BOT2', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN3)

print("[KHUNI] Starting Fourth SpamBot") 
BOT3 = TelegramClient('BOT3', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN4)

print("[KHUNI] Starting Fifth SpamBot") 
BOT4 = TelegramClient('BOT4', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN5)

print("[KHUNI] Starting Sixth SpamBot") 
BOT5 = TelegramClient('BOT5', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN6)

print("[KHUNI] Starting Seventh SpamBot") 
BOT6 = TelegramClient('BOT6', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN7)

print("[KHUNI] Starting Eighth SpamBot") 
BOT7 = TelegramClient('BOT7', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN8)

print("[KHUNI] Starting Ninth SpamBot") 
BOT8 = TelegramClient('BOT8', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN9)

print("[KHUNI] Starting Tenth SpamBot") 
BOT9 = TelegramClient('BOT9', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN10)

print("[INFO] Successfully Started Bot Client Now Loading Plugins!") 
