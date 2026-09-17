import os
import asyncio
from highrise import BaseBot, __main__

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot successfully started and connected")

    async def on_user_join(self, user) -> None:
        pass

    async def on_chat(self, user, message: str) -> None:
        if message.lower() == "!ping":
            await self.highrise.chat(f"Pong !")
        elif message.lower() == "!dance":
            await self.highrise.send_emote("emote-kiss")
        elif message.lower() == "!hi":
            await self.highrise.chat(f"Hello !")

if __name__ == "__main__":
    room_id = os.getenv("ROOM_ID")
    token = os.getenv("BOT_TOKEN")
    
    # Highrise ke standard CLI command ko python ke andar se chalane ke liye
    import sys
    from highrise.__main__ import main as highrise_cli
    
    sys.argv = ["highrise", "main:MyBot", "--room-id", room_id, "--token", token]
    asyncio.run(highrise_cli())
            
