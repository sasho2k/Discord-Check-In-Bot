import random
from datetime import datetime
import discord
from discord.ext import tasks
# noinspection PyUnresolvedReferences
import client.dialogue

"""
# This file will be the top layer of our program. We can keep it simple with a single class and run() function.
# All supporting functions are imported from our other files.

"""


# This is our client class.
class MyClient(discord.Client):
    # Set the states on initialization.
    today_date = ""
    user_list = []

    # The simple on-ready function where our tasks will live.
    async def on_ready(self):
        print('CLIENT: Logged on and running as {0}.\n'.format(self.user))
        self.check_date.start()

    # Check to see if the current date has changed to empty the user_list.
    @tasks.loop(minutes=1)
    async def check_date(self):
        if datetime.now().strftime("%d") != self.today_date:
            print('CLIENT: Changing self.today_date from {0} to {1}\nEditing user_list to empty.\n'.format(self.today_date, datetime.now().strftime("%d")))
            self.today_date = datetime.now().strftime("%d")
            self.user_list = []

    async def on_message(self, message):
        # Dont respond to ourselves lol.
        if message.author == self.user:
            return

        if message.content.startswith('check in') or message.content.startswith('checking in'):
            # If user is in the list already, send out a msg and return. Else, add them to our list and send a msg.
            for user in self.user_list:
                if message.author.name == user:
                    await message.channel.send(
                        client.dialogue.already_checked_in[random.randint(0, len(client.dialogue.already_checked_in)-1)])
                    return

            self.user_list.append(message.author.name)
            await message.channel.send(
                client.dialogue.checking_in[random.randint(0, len(client.dialogue.already_checked_in) - 1)])