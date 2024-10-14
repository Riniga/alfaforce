import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_dir, '..'))

import bots as bot
import tools
import os
from dotenv import load_dotenv
load_dotenv()

wake_word = 'echo'
listener_bot = bot.ListenerBot()
transcriber_bot = bot.TranscriberBot()

def audio_recieved(audio_path):
    prompt_text = transcriber_bot.wav_to_text(audio_path)
    print (f'Recieved text: {prompt_text}')
    clean_prompt = tools.contains_word(prompt_text, wake_word)
    if (clean_prompt==None): print('Audio did NOT contain the wake word')
    else: print (f'C leaned text: {clean_prompt}')


print('\nSay ', wake_word, ' followed with your prompt\n')
listener_bot.start_listening(audio_recieved)