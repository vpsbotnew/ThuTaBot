#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int("22270429")

API_HASH = "3e2e8f8f0ae56bb0998c264c4ca243cb"

BOT_TOKEN = "5987017187:AAGm6XTEvGilHtD8RwVutuW67S2VDTpr_mI"

DB_URI = "mongodb+srv://thutabot:thutabot@thutabot.af0m6jc.mongodb.net/?retryWrites=true&w=majority"

USER_SESSION = "BQATjqidhwRn8_7JhVYT9WVrkS5QPRGq8qm658ZkhgxAKz_CqXOCPk24rT_NJ80rBc5SSF2hQeAz-j7E-MEMdJ82Qs5DalCYpU6R9JUrEVX7KYd370N3W2-P64CW2yJvp8HlRl-h7_VUbdYNrUkpCYPyXGL60BPG7Je1etP1kY9x3PeAG4a8U2xccmfeMZ0z5e76ejDdRLbukChZ2c23mV5iKcjD825U7jKGsbbZ7OSSfp1X4A4LzZxzUyghhVegUGkgV8yxaeEzQQlia2FnMsfMte-nYvT3V-ifHi1deGDsfXFRgdeUto0bLzKCkIzhDJWHbhkWiOUVZm5cN7PExW9mAAAAAWIw7noA"

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
