import os
import subprocess
from highrise import BaseBot

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
    
    # Ab yeh teeno arguments ek sath properly pass honge
    subprocess.run(["highrise", "main.py", "MyBot", room_id, token])
    
