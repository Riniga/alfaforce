# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
from bot_factory import BotFactory


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        
        text = turn_context.activity.text
        if text.startswith("@"):
            name = text.split(" ")[0][1:]
            text = " ".join(text.split(" ")[1:])
            bot = BotFactory.get_bot(name)
            response = bot.ask( text )
            await turn_context.send_activity(response)

        else:
            # Send a message to the user with the text
            await turn_context.send_activity(f"You must mention a teammate to ask them.")

        


    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("""**👋 Welcome!**

You have the following members in your team:

- **Ragnar** — Specifies requirements  
- **Sara** — Helps you with the project  
- **Chad** — Can chat about anything

💡 *Mention anyone in your team using* `@name` *to ask them something.*""")
