
from dotenv import load_dotenv
from chatbot import ChatBot
from dispatcher import DispatcherBot
from imageanalyzerbot import ImageAnalyzerBot
from speechbot import SpeechBot
from listenerbot import ListenerBot
from sensors import Sensors
import os

load_dotenv()

chat_bot = ChatBot(os.getenv('GROQ_API_KEY'))
dispatcher_bot = DispatcherBot(os.getenv('GROQ_API_KEY'))
imageAnalyzerBot = ImageAnalyzerBot(os.getenv('GOOGLEAI_API_KEY') )
speechBot = SpeechBot(os.getenv('OPENAI_API_KEY') )
listenerBot = ListenerBot('echo')
sensors = Sensors()

def callback(recognizer, audio):
    print ('callback called')
    prompt_audio_path = 'prompt.wav'
    with open(prompt_audio_path, 'wb') as f:
        f.write(audio.get_wav_data() )
    prompt_text = listenerBot.wav_to_text(prompt_audio_path)
    print (f'recieved text: {prompt_text}')
    clean_prompt = listenerBot.extract_prompt(prompt_text)

    if clean_prompt:
        print(f'USER: {clean_prompt}')
        call = dispatcher_bot.ask(clean_prompt)

        if 'take snapshot' in call:
            print('Taking screenshot')
            sensors.take_screenshot()
            visual_context=imageAnalyzerBot.ask(prompt=clean_prompt, photo_path="screenshot.jpg")
        elif 'capture webcam' in call:
            print('Capture photo from webcam')
            sensors.web_cam_capture()
            visual_context=imageAnalyzerBot.ask(prompt=clean_prompt, photo_path="webcam.jpg")
        elif 'extract clipboard':
            print('Copying clipboard text')
            paste = sensors.get_clipboard_text()
            clean_prompt = f'{clean_prompt}\n\n CLIPBOARD CONTENT: {paste}'
            visual_context=None
        else:
            visual_context=None
        response = chat_bot.ask(prompt=clean_prompt, img_context=visual_context) 
        print(f'ASSISTANT: {response}')
        speechBot.speak(response)

listenerBot.start_listening(callback)