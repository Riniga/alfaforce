import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_dir, '..'))
import bots as bot

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:9000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_bot = bot.ChatBot(os.getenv('GROQ_API_KEY'))
 
@app.get("/chatbot")
async def get_data(query = None):
    response = chat_bot.ask(query, None)
    return {"message": response}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    print("Upload recived!")
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    imageAnalyzer = bot.ImageAnalyzerBot(os.getenv('GOOGLEAI_API_KEY'))
    response = imageAnalyzer.ask("Describe the content", file_path)
    return {"message": response}


# uvicorn chatbot:app --reload --host 0.0.0.0 --port 5000
# curl http://localhost:5000/api?query=vad%20heter%20jag



