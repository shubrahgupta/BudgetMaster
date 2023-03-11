import numpy as np
from fastapi import FastAPI, Form
import pandas as pd
from starlette.responses import HTMLResponse
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import model
import re

def parseInt(text):
    arr = [int(s) for s in re.findall(r'\d+', text)]
    try:
        return arr[0]
    except IndexError:
        return 0


app = FastAPI()


@app.get('/')  # basic get view
def basic_view():
    return {"WELCOME": "GO TO /docs route, or /post or send POST request to /entry "}

@app.get('/entry', response_class=HTMLResponse)
def take_input():
    return '''
        <form method="post">
        <input maxlength="28" name="text" type="text" />
        <input type="submit" />'''

@app.post('/entry')
def input_analysis(text: str = Form(...)):
    loaded_model = tf.keras.models.load_model('budgetMaster_chatbot.h5')

    intents = model.Pclass(text, model.newWords, model.ourClasses, loaded_model)
    ourResult = model.getRes(intents, model.ourData)
    # ourResult.append(text)
    ourResult["log"] = text
    ourResult["amount"] = parseInt(text)


    return ourResult





