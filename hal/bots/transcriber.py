from faster_whisper import WhisperModel
import speech_recognition as sr
import os
import re
import time

class TranscriberBot:
    def __init__(self):
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
    

