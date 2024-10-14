import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_dir, '..'))

import bots as bot
import os
from dotenv import load_dotenv
load_dotenv()

chat_bot = bot.SpeechBot(os.getenv('OPENAI_API_KEY'), bot.SpeechBot.Voice.alloy)
response = chat_bot.speak("I am a millionare")
