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

BOT_TOKEN = "5989078394:AAFX3-bU_4_8NeM8d2q2TEknJ_SCU45d9GI"

DB_URI = "mongodb+srv://ynmoviefilter:ynmoviefilter@cluster0.6erlpc6.mongodb.net/?retryWrites=true&w=majority"

USER_SESSION = "BQDCa1DUZ6h4Yb4znhffXZzxtRCSYHE1-u0jDUPeuRRKuqEzCZPm3gRjulYYQs9tU3yRhMxpaYB2ju2AnjB50Y-uCd6EaOyRRtfNoSp7hbevc1KNbZlm4MHL2pSTjaEs7aCTV2oQTolOWOH9NwFOkBwPFVc37pQxJQV82hYXGLknIxdap9Sz88pxNdWhb82FWIwrecjfdKVu2OwGBPV6wdPF2MfJ9xL5DqaWqsJ4oA3qlPkfhrzNToT9EO_EeQCl1_V8GO59HCGKKmHBWOtZQdyUrRiq3ToRJdPQ1ahhpZu9CgjX8tr8BSsZ8EzXk4kRWZ9Vik-5-rrlmwoXdYXLGmRnUFsxVQA"

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
