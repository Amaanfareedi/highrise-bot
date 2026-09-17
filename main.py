import asyncio
from highrise import BaseBot, __main__

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot successfully started and connected to Highrise!")
        
    async def on_user_join(self, user) -> None:
        # Greeter Feature: Jaise hi koi room mein aaye, welcome karo
        await self.highrise.chat(f"Welcome to the room, {user.username}! 🎉")
        
    async def on_chat(self, user:- user, message: str) -> None:
        # Entertainment & Moderation Feature
        if message.lower() == "!ping":
            await self.highrise.chat(f"Pong! 🏓 {user.username}")
        elif message.lower() == "!dance":
            await self.highrise.send_emote("emote-dance-loop", user.id)
        elif message.lower() == "!hi":
            await self.highrise.chat(f"Hello {user.username}! Kaisa chal raha hai?")

if __name__ == "__main__":
    import os
    # Render ke liye zaroori setup
    asyncio.run(__main__.main(MyBot(), room_id="ROOM_ID_YAHAN_DALO", token="BOT_API_TOKEN_YAHAN_DALO"))
                                           
