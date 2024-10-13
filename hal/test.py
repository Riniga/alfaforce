import cv2
import pyperclip
import pyaudio
import os
from openai import OpenAI
from dotenv import load_dotenv
from dispatcher import DispatcherBot
from chatbot import ChatBot


load_dotenv()

def web_cam_capture():
    web_cam = cv2.VideoCapture(0)
    if not web_cam.isOpened():
        print('Error: Camera dod not open successfully')
        exit()
    path = 'webcam.jpg'
    ret, frame = web_cam.read()
    cv2.imwrite(path, frame)

def get_clipboard_text():
    clipboard_content = pyperclip.paste()
    if  isinstance(clipboard_content, str):
        return clipboard_content
    else:
        print('No clipboard text to copy')
        return None
    
def speak(text):
    openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    player_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)
    stream_start = False
    with openai_client.audio.speech.with_streaming_response.create(model='tts-1', voice='echo', response_format='pcm', input=text) as response:
        silence_threshold = 0.01
        for chunk in response.iter_bytes(chunk_size = 1024):
            if stream_start:
                player_stream.write(chunk)
            else:
                if max(chunk) > silence_threshold:
                    player_stream.write(chunk)
                    stream_start=True

#speak("My name is Hal9000")

dispatcher_bot = DispatcherBot(os.getenv('GROQ_API_KEY'))
chat_bot = ChatBot(os.getenv('GROQ_API_KEY'))
print (dispatcher_bot.ask("What is the code I have in memory"))

#print(chat_bot.ask("What book have Ada Lovlace written"))

