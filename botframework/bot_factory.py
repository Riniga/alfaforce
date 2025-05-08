import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_dir, '../hal'))

import bots as bot
from dotenv import load_dotenv
load_dotenv()


class BotFactory:
    @staticmethod
    def get_bot(bot_name: str):
        bot_name = bot_name.lower()
        if bot_name == "ragnar":
            return bot.RequirementBot(os.getenv('GROQ_API_KEY'))
        elif bot_name == "sara":
            return bot.ScrummasterBot(os.getenv('GROQ_API_KEY'))
        elif bot_name == "chad":
            return bot.ConversationBot(os.getenv('GROQ_API_KEY'))
         

