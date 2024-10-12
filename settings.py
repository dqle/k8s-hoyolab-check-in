import os
import json
import logging
from dotenv import load_dotenv
from logging.config import dictConfig

load_dotenv()
URL_CHECKIN_LIST = {
    "genshin_impact"   : "https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us&act_id=e202102251931481",
    "honkai_star_rail" : "https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=en-us&act_id=e202303301540311",
    "honkai_impact_3rd": "https://sg-public-api.hoyolab.com/event/mani/sign?lang=en-us&act_id=e202110291205111",
    "tears_of_themis"  : "https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=en-us&act_id=e202308141137581",
    "zenless_zone_zero": "https://sg-public-api.hoyolab.com/event/luna/zzz/os/sign?lang=en-us&act_id=e202406031448091"
}

#-----------------------------------------
# Helm Vars
#-----------------------------------------

ENABLED_DISCORD_WEBHOOK = os.getenv("ENABLED_DISCORD_WEBHOOK")
DISCORD_WEBHOOK         = os.getenv("DISCORD_WEBHOOK")
CHECK_IN                = json.loads(os.getenv("CHECK_IN", "{}"))
LTOKEN_V2               = os.getenv("LTOKEN_V2")
LTUID_V2                = os.getenv("LTUID_V2")

#-----------------------------------------
# LOG CONFIG
#-----------------------------------------

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(levelname)-10s - %(name)-15s : %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "bot": {"handlers": ["console"], "level": "INFO", "propagate": False},
    },
}

dictConfig(LOGGING_CONFIG)