from fastapi import FastAPI, Form, Request, status, Response
from starlette.responses import HTMLResponse
from starlette.datastructures import URL
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import tensorflow as tf
import model
import re
from fastapi.responses import RedirectResponse

def parseInt(text):
    arr = [int(s) for s in re.findall(r'\d+', text)]
    try:
        return arr[0]
    except IndexError:
        return 0


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')


@app.get('/')  # basic get view
def basic_view():
    return {"WELCOME": "GO TO /docs route, or /entry or send POST request to /entry "}

@app.get('/entry', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('home.html',{'request': request})
    
    # return '''
    #     <form method="post">
    #     <input maxlength="28" name="text" type="text" />
    #     <input type="submit" />'''

# @app.post('/submitFinal')
@app.post('/entry')
async def input_analysis(text: str = Form(...)):
    loaded_model = tf.keras.models.load_model('budgetMaster_chatbot.h5')

    intents = model.Pclass(text, model.newWords, model.ourClasses, loaded_model)
    ourResult = model.getRes(intents, model.ourData)
    # ourResult.append(text)
    ourResult["log"] = text
    ourResult["amount"] = parseInt(text)
    # headers = {'Location': '/submitFinal'}
    # return Response(content=ourResult, headers=headers, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    # if ourResult["tag"] == "gibberish":
    #     return {our}
    print(ourResult)
    return ourResult

# @app.post('/submitFinal')
# def final(msg: str = Form(...)):
#     return f'{msg}'







