import os


class Config(object):
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    USER = os.environ.get("USER")
