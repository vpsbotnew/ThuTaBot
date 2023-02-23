#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int("12158462")

API_HASH = "0b962717d931f4480c46d56c85d409a5"

BOT_TOKEN = "6105683190:AAG3RQFXa_LArBNeuyIDuXkL_j-vaKwp0Hk"

DB_URI = "mongodb+srv://pmfilter:pmfilter@cluster0.xvulgll.mongodb.net/?retryWrites=true&w=majority"

USER_SESSION = "BQAnm8T-4nJI42k_XyHzcqlF0mtk8IyNJ02MQuNbhTP82Lp-wcjzhiGFIUSYI6HXxAHi9wNdRUnqz2Uc7fVcQILkARaPKT_0HUr9Q2zqyesEv6V7KG3oQtT-arJgar8p7gPQfb5S6m822eO6gfxTt-_V1xJ0dmBW3v4zeycVGMrKgJ5flhBt2cHh_mgwt9W1m3jbm5Ids8Ch5CEnhoM7_U8FQKGP4WGUB9SbNLkw3bbKmb_HOFxr55tSwhw6qvuL-ZJ_IeJ_uGSiIcklhkR8-qs85XZ2SiyeWCt49T5IAQAr2TvAfi2i8cmq4pqOCORlkH9QJyrAKjNgwKGDxXbbwKxTUFsxVQA"

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
