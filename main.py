import requests
import settings
from discordwebhook import Discord

logger = settings.logging.getLogger("bot")

#-----------------------------------------
# Craft Token
#-----------------------------------------

TOKEN = f"ltoken_v2={settings.LTOKEN_V2}; ltuid_v2={settings.LTUID_V2};"

#-----------------------------------------
# Craft Header
#-----------------------------------------

HEADER = {
    'Cookie': TOKEN,
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'x-rpc-app_version': '2.59.0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36',
    'x-rpc-client_type': '4',
    'Referer': 'https://act.hoyolab.com/',
    'Origin': 'https://act.hoyolab.com'
  }

#-----------------------------------------
# Discord Setup
#-----------------------------------------
if settings.ENABLED_DISCORD_WEBHOOK:
    discord = Discord(url=settings.DISCORD_WEBHOOK)

#-----------------------------------------
# Send POST for daily check in
#-----------------------------------------

def check_in(game):
    response = requests.post(settings.URL_CHECKIN_LIST[game], headers=HEADER)

    if response.status_code == 200:
        response_data = response.json()
        message = response_data.get("message", "No message found")
        logger.info(message)
        if settings.ENABLED_DISCORD_WEBHOOK:
            discord.post(content=f":white_check_mark: Checked in for {game.replace("_", " ").title()} : {message}")
    else:
        error = f"Request failed with status code: {response.status_code}"
        logger.error(error)
        if settings.ENABLED_DISCORD_WEBHOOK:
            discord.post(content=f":x: Checked in for {game} : {error}")

# Sending the POST request
if settings.CHECK_IN["genshin_impact"]:
    check_in("genshin_impact")
elif settings.CHECK_IN["honkai_star_rail"]:
    check_in("honkai_star_rail")
elif settings.CHECK_IN["honkai_impact_3rd"]:
    check_in("honkai_impact_3rd")
elif settings.CHECK_IN["tears_of_themis"]:
    check_in("tears_of_themis")
elif settings.CHECK_IN["zenless_zone_zero"]:
    check_in("zenless_zone_zero")
else:
    logger.info("No game selected")
    if settings.ENABLED_DISCORD_WEBHOOK:
        discord.post(content=":x: No game selected")
