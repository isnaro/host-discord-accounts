import discord
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve tokens and voice channel ID from environment variables
TOKENS = [
    os.getenv('TOKEN_1'),
    os.getenv('TOKEN_2'),
    # Add more tokens as needed
]

VOICE_CHANNEL_ID = int(os.getenv('VOICE_CHANNEL_ID'))

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel = self.get_channel(VOICE_CHANNEL_ID)
        if channel and isinstance(channel, discord.VoiceChannel):
            await channel.connect()

async def main():
    clients = []
    for token in TOKENS:
        if token:
            client = MyClient()
            clients.append(client)
            asyncio.create_task(client.start(token, bot=False))
    
    # Keep the script running
    while True:
        await asyncio.sleep(1)

asyncio.run(main())
