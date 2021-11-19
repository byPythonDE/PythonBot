import discord
import os
import json

client = discord.Client()


@client.event
async def on_ready():
	print("Logged in as: {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/hello"):
        await message.channel.send("Hello there!")

client.run(os.getenv("TOKEN"))