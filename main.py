import os
from highrise import BaseBot
from highrise.__main__ import BotDefinition

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print(f"Bot connected to {session_metadata.room_info.room_name}!")
        # Bot join karte hi msg karega
        await self.highrise.chat("Bot Online! Type !ping")

    async def on_user_join(self, user) -> None:
        await self.highrise.chat(f"Welcome {user.username} to the room!")

    async def on_chat(self, user, message: str) -> None:
        msg = message.lower()
        
        if msg == "!ping":
            await self.highrise.chat(f"Pong! @{user.username}")
        
        elif msg == "!hi":
            await self.highrise.chat(f"Hello @{user.username}!")
            
        elif msg == "!dance":
            await self.highrise.send_emote("dance", user.id)

# Bot ko run karne ke liye ye sabse important hai
if __name__ == "__main__":
    BotDefinition(MyBot()).run()
