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
            
