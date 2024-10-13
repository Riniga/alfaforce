from openai import OpenAI
import pyaudio


class SpeechBot:
    def __init__(self, key):
        self.openai_client = OpenAI(api_key=key)


    def speak(self,text):
        player_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)
        stream_start = False

        with self.openai_client.audio.speech.with_streaming_response.create(model='tts-1', voice='echo', response_format='pcm', input=text) as response:
            silence_threshold = 0.01
            for chunk in response.iter_bytes(chunk_size = 1024):
                if stream_start:
                    player_stream.write(chunk)
                else:
                    if max(chunk) > silence_threshold:
                        player_stream.write(chunk)
                        stream_start=True

    voices = ['shimmer', 'nova', 'onyx', 'fable', 'echo', 'alloy']
