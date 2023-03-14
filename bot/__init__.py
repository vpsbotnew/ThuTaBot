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

DB_URI = "mongodb+srv://new_user_user1212:thuta12345@cluster0.lhmmymb.mongodb.net/?retryWrites=true&w=majority"

USER_SESSION = "BQCdymFRVO0bOnBfxe0RAgV-sTohYR1kq4lSPaDxSYO6JLIk8L5aQ5SLW52z32gCuR6NTi6fOuP4Gqd8EILrdvC90CSnmX_iw4_XJw75z6k9XNz58Hhgl7bTWJGo_4JbeGdzsTRZS7uOh7ElSPW5uPbOOkaYH9uuHpRkP4sCt3qhh6E7lXM8rz6QNQ2jN2e-H64BTs_FPKQbT9nEgpU8RaQqP1qSNgj7SmiKJdR528hmqNxjNe9CrlZ27uUmJhtxoIiaC3T0cT-wYJaeLOZ6eGU3rHjkik6vG_oNTy0zWhlNbW3gbSxbsAvCZwOeyXCnTAK1ZPELkegc36i5aoWYx_IuUFsxVQA"

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
