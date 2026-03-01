from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
import re

app = FastAPI(title="Text Analyzer API")

class TextRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Text Analyzer API Running"}

@app.post("/analyze")
def analyze_text(data: TextRequest):
    text = data.text
    
    words = len(text.split())
    characters = len(text)
    sentences = len(re.findall(r'[.!?]+', text))

    return {
        "word_count": words,
        "character_count": characters,
        "sentence_count": sentences
    }

lambda_handler = Mangum(app)