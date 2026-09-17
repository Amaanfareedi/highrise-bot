from highrise import BaseBot

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot Online! Connected to room")
        await self.highrise.chat("Bot Online! Commands: !ping, !hi, !dance")

    async def on_user_join(self, user) -> None:
        await self.highrise.chat(f"Welcome {user.username}!")

    async def on_chat(self, user, message: str) -> None:
        msg = message.lower().strip()
        if msg == "!ping":
            await self.highrise.chat(f"Pong @{user.username}")
        elif msg == "!hi":
            await self.highrise.chat(f"Hello @{user.username}!")
        elif msg == "!dance":
            await self.highrise.send_emote("dance-tiktok", user.id)
