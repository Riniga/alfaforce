from groq import Groq

## Trying to determin if the user intend to use:
# * extract content from the clipboard, 
# * whants to take a snapchot of the screen or 
# * take a picture with the web camera
# Returns a short message what is intended, non if it is unable to determin the intension.

class DispatcherBot:
    def __init__(self, key):
        self.groq_client = Groq(api_key=key )
        self.sys_msg=(
            'You are an AI function calling model. You will determine wheter extracting the users clipboard content, '
            'taking a screenshot, capturing the webcam or calling no functions is best for a voice assistant to respond '
            'to the users prompt. The webcam can be assumed to be a normal laptop webcam facing the user. You will '
            'respond with only one selection from this list: ["extract clipboard", "take snapshot", "capture webcam", "None"] \n'
            'Do not respond with anything but the most logical selection from that list with no explanations. Format the '
            'function call name exactly as I listed.'
        )
        self.convo = [{'role':'system','content':self.sys_msg}]
        
    
    def ask(self, prompt):
        self.convo.append({'role':'user','content':prompt})
        chat_completion=self.groq_client.chat.completions.create(messages=self.convo, model='llama3-70b-8192')
        response = chat_completion.choices[0].message
        return response.content