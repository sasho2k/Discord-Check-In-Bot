from datetime import datetime
import discord
from client.client import MyClient
from internal_settings.internal import get_settings


def run():
    client = MyClient(intents=discord.Intents.all())
    print("\nStarting Process...\n")
    token = get_settings()
    client.today_date = datetime.now().strftime("%d")

    try:
        print("CLIENT: Starting run process.\n")
        client.run(token)
    except discord.errors.HTTPException:
        print("FATAL: Invalid token.\n")
        exit(0)
    except discord.errors.LoginFailure:
        print("FATAL: Invalid token.\n")
        exit(0)
