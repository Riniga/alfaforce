from groq import Groq
# create parent  of type GroqBot
class ChatBot:
    def __init__(self, key):
        self.groq_client = Groq(api_key=key )
        self.sys_msg = (
            'You are a multi-modal AI voice assistant. Your user may or may not have attached a photo for context '
            '(either a screenshot or a webcam capture). Any photo has already been processed into a highly detailed '
            'text prompt tht will be attached to their transcribed voice prompt. Generate the most useful and '
            'factural response possible, carfully considering all previous generated text in your response before '
            'adding new tokens to the response. Do not expect or request images, just use context if added. '
            'Use all of the context of this conversation so your response is relevant to the conversation. Make '
            'your response clear and concise, avoid any verbosity'
        )
        self.convo = [{'role':'system','content':self.sys_msg}]

    def ask(self, prompt):
        convo = [{'role':'user','content':prompt}]
        chat_completion=self.groq_client.chat.completions.create(messages=convo, model='llama3-70b-8192')
        response = chat_completion.choices[0].message
        return response.content

    def ask(self, prompt, img_context):
        if img_context:
            prompt = f'USER PROMPT: {prompt}\n\n  IMAGE CONTEXT: {img_context}'
        self.convo.append({'role':'user','content':prompt})
        chat_completion=self.groq_client.chat.completions.create(messages=self.convo, model='llama3-70b-8192')
        response = chat_completion.choices[0].message
        self.convo.append(response)
        return response.content