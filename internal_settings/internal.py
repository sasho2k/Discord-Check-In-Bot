# This grabs the token and channel from the settings json file but not before parsing and checking them.
# If there is no settings.json file, then throw a fatal error since these are essential to our bot.
import json
import os
from os.path import exists


def get_settings():
    path = ""

    if exists("internal_settings/settings.json"):
        path = 'internal_settings/settings.json'
    elif exists(os.getcwd() + "/settings.json"):
        path = os.getcwd() + "/settings.json"
    else:
        print('FATAL: No settings.json file found.\n')
        if exists("example_settings.json"):
            print('FATAL : Replace the example_settings.json with a settings.json file, then fill it with your info.')
        exit(0)

    with open(path) as f:
        json_data = json.load(f)
    f.close()

    token = check_token(json_data)
    bot_prefix = check_bot_prefix(json_data)
    if (token is not None) and (bot_prefix is not None):
        return token, bot_prefix
    else:
        exit(0)


def check_token(json_data):
    if 'token' in json_data:
        print("Token:", json_data.get('token'))

        if json_data.get('token').strip() != "":
            return json_data['token']
        else:
            print("FATAL: Empty token value.")
            return None
    else:
        print("FATAL: Missing token value from settings.json.")
        return None


def check_bot_prefix(json_data):
    if 'bot_prefix' in json_data:
        print("Bot Prefix:", json_data.get('bot_prefix'))

        if json_data.get('bot_prefix').strip() != "":
            return json_data['bot_prefix']
        else:
            print("FATAL: Empty bot prefix value.")
            return None
    else:
        print("FATAL: Missing bot prefix value from settings.json.")
        return None
