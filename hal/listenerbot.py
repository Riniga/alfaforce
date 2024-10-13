from faster_whisper import WhisperModel
import speech_recognition as sr
import os
import re
import time

class ListenerBot:
    def __init__(self, wake_word):
        self.wake_word=wake_word
        num_cores = os.cpu_count()
        whisper_size = 'base'
        self.whisper_model = WhisperModel(
            whisper_size,
            device='cpu',
            compute_type='int8',
            cpu_threads=num_cores//2,
            num_workers=num_cores//2
        )
        self.r = sr.Recognizer()
        self.source = sr.Microphone()

    def wav_to_text(self, audio_path):
        print ('conveting audio to text')
        segments, _ = self.whisper_model.transcribe(audio_path)
        text = ''.join(segment.text for segment in segments)
        return text
    
    def start_listening(self, callback):
        with self.source as s:
            self.r.adjust_for_ambient_noise(s, duration=2)
        print('\nSay ', self.wake_word, ' followed with your prompt\n')
        self.r.listen_in_background(self.source, callback)
        while True:
            time.sleep(0.5)

    def extract_prompt(self,transcribed_text):
        pattern = rf'\b{re.escape(self.wake_word)}[\s,.?!]*([A-Za-z0-9].*)'
        match = re.search(pattern, transcribed_text, re.IGNORECASE)
        if match:
            prompt = match.group(1).strip()
            return prompt
        else:
            return None