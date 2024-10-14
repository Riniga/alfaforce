from faster_whisper import WhisperModel
import speech_recognition as sr
import os
import re
import time

class ListenerBot:
    def __init__(self):
        self.r = sr.Recognizer()
        self.source = sr.Microphone()
        self.external_callback = None

    def save_audio_and_forward(self, recognizer, audio):
        prompt_audio_path = 'prompt.wav'
        with open(prompt_audio_path, 'wb') as f: f.write(audio.get_wav_data() )
        self.external_callback(prompt_audio_path)

    def start_listening(self, callback=None):
        self.external_callback = callback
        with self.source as s: self.r.adjust_for_ambient_noise(s, duration=2)
        self.r.listen_in_background(self.source, self.save_audio_and_forward)
        while True: time.sleep(0.5)