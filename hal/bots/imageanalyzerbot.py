from PIL import Image
import google.generativeai as genai

# Analyzes an image and returns a description

class ImageAnalyzerBot:
    def __init__(self, key):
        self.sys_msg = prompt = (
            'Your are the vision analysis AI that provides semantic meaning from images to provide context '
            'to send to another AI that will create a response to the user. Do not respond as the AI assistant '
            'to the user. Instead take the user prompt input and try to extract all meaning from the photo '
            'relevant to the user prompt. Then generate as much objective data about the image for the AI '
            'assistant who will respond to the user. '
        )
        self.generation_config = {
            'temperature': 0.7,
            'top_p': 1,
            'top_k': 1,
            'max_output_tokens': 2048
        }
        self.safety_settings = [
            {
                'category':'HARM_CATEGORY_HARASSMENT',
                'threshold': 'BLOCK_NONE'
            },
            {
                'category':'HARM_CATEGORY_HATE_SPEECH',
                'threshold': 'BLOCK_NONE'
            },
            {
                'category':'HARM_CATEGORY_SEXUALLY_EXPLICIT',
                'threshold': 'BLOCK_NONE'
            },
            {
                'category':'HARM_CATEGORY_DANGEROUS_CONTENT',
                'threshold': 'BLOCK_NONE'
            },
        ]
        
        genai.configure(api_key=key)
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest', generation_config=self.generation_config, safety_settings=self.safety_settings)
        self.convo = [{'role':'system','content':self.sys_msg}]

    def ask(self, prompt, photo_path):
        img=Image.open(photo_path)
        prompt = (
            self.sys_msg + f'\n USER PROMPT: {prompt}'
        )
        response= self.model.generate_content([prompt, img])  
        return response.text
