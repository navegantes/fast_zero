from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/helloworld', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def html_response():
    html_resp = """<h1>Olá Mundo!</h1>"""
    return HTMLResponse(content=html_resp)
