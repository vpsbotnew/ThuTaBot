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

USER_SESSION = "BQBkZBGLgEukQ8PHW22lQRCTKYh0EDhbWbk3TFlQXFSuU0v33mm3Hh-vOK9ejhWBAUHk1-rAezUq9BEGSQKcA8PbyzT98zG8E6rA_uhjmts4MdhkLvqa57Hfj0wAGAKfz920pfA8IOlF-Dbhgx7F0fzgl9jKTPkUKKCQFUMdq2dtoO6e06LUUlDt5MFJaRMjwNcKXhRNmCeIF7KaWkukc6IL36CeV3h9kcipwt5ixujBx_6_CMuVInYYT3OPdXkdSgc9VPdLQjY2fTtfYwYo4BNac9rh7esldq0t5nUygit0eokY7ICkkxtbWbapE8RLufot9tfCrGUdbZmdffmup138UFsxVQA"

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
