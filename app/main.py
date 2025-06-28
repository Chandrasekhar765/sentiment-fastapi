from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/sentiment")
def get_sentiment(input: TextInput):
    blob = TextBlob(input.text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {"sentiment": sentiment}
