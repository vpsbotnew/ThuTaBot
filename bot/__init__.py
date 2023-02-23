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

USER_SESSION = "BQAa_inVJMNV0w07gWAQDK4zb751K5EP0v7l5lb1pqfPSJkuvjCTkNLl3V5B0dcPF63THmyCy_vxdYjFAQrlwHvJhfic5cdc7Lvhd0L4lSpmQcl7dLIJoxK3Q9TPS7tgToQuwEwIyjf_BKTYdsi6fkSOSRqSzcubicZmQGTbfVunhvnSgyH5TX1ezgydjY8jrkdMZZPE0LyVLtL562ZxDiOziS4xzv5S6nihY409QRAxKRhBgV6tEL6TRZWL_Jf2JVAsD65pv1VVg8pK1VaBoDvaduhY7TUxS3tPavYG5NIAjuEqGExP8rklk7rcwlgwbbTpZEAD6_V6NG2zFfYOTRDEUFsxVQA"

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
