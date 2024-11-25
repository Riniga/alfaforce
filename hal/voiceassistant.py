
from dotenv import load_dotenv
import os
import tools
import bots as bot

load_dotenv()

wake_word = 'echo'

# Bots need for the job
listener_bot = bot.ListenerBot()
transcriber_bot = bot.TranscriberBot()
dispatcher_bot = bot.DispatcherBot(os.getenv('GROQ_API_KEY'))
imageAnalyzerBot = bot.ImageAnalyzerBot(os.getenv('GOOGLEAI_API_KEY') )
chat_bot = bot.ChatBot(os.getenv('GROQ_API_KEY'))
speechBot = bot.SpeechBot(os.getenv('OPENAI_API_KEY'), bot.SpeechBot.Voice.shimmer )

def audio_recieved(audio_path):
    prompt_text = transcriber_bot.wav_to_text(audio_path)
    clean_prompt = tools.contains_word(prompt_text, wake_word)
    if clean_prompt:
        print(f'USER: {clean_prompt}')
        call = dispatcher_bot.ask(clean_prompt)
        if 'take snapshot' in call:
            print('Taking screenshot')
            tools.take_screenshot()
            visual_context=imageAnalyzerBot.ask(prompt=clean_prompt, photo_path="screenshot.jpg")
        elif 'capture webcam' in call:
            print('Capture photo from webcam')
            tools.web_cam_capture()
            visual_context=imageAnalyzerBot.ask(prompt=clean_prompt, photo_path="webcam.jpg")
        elif 'extract clipboard':
            print('Copying clipboard text')
            paste = tools.get_clipboard_text()
            clean_prompt = f'{clean_prompt}\n\n CLIPBOARD CONTENT: {paste}'
            visual_context=None
        else:
            visual_context=None
        response = chat_bot.ask(prompt=clean_prompt, img_context=visual_context) 
        print(f'ASSISTANT: {response}')
        speechBot.speak(response)

listener_bot.start_listening(audio_recieved)