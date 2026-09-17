from highrise import BaseBot
from highrise.__main__ import BotDefinition

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot Online!")
        await self.highrise.chat("Bot is Online! !ping likho")

    async def on_user_join(self, user) -> None:
        await self.highrise.chat(f"Welcome {user.username}!")

    async def on_chat(self, user, message: str) -> None:
        if message.lower() == "!ping":
            await self.highrise.chat(f"Pong @{user.username}")
        elif message.lower() == "!hi":
            await self.highrise.chat(f"Hello @{user.username}")

if __name__ == "__main__":
    BotDefinition(MyBot()).run()
