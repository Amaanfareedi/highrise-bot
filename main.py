import os
from highrise import BaseBot
from highrise.__main__ import BotDefinition

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot Online! Connected")
        await self.highrise.chat("Bot Online! !ping / !hi likho")

    async def on_user_join(self, user) -> None:
        await self.highrise.chat(f"Welcome {user.username}!")

    async def on_chat(self, user, message: str) -> None:
        if message.lower() == "!ping":
            await self.highrise.chat(f"Pong @{user.username}")
        elif message.lower() == "!hi":
            await self.highrise.chat(f"Hello @{user.username}!")
        elif message.lower() == "!dance":
            await self.highrise.send_emote("dance", user.id)

if __name__ == "__main__":
    # Ye Render ke Environment se ID/Token lega
    ROOM_ID = os.getenv("ROOM_ID")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    if not ROOM_ID or not BOT_TOKEN:
        print("ERROR: ROOM_ID ya BOT_TOKEN Environment Variable me nahi mila!")
    else:
        BotDefinition(MyBot(), ROOM_ID, BOT_TOKEN).run()
