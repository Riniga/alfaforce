import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_dir, '..'))

import bots as bot
import os
from dotenv import load_dotenv
load_dotenv()

chat_bot = bot.DispatcherBot(os.getenv('GROQ_API_KEY'))
response = chat_bot.ask("What do the code in memory do")
print(response)