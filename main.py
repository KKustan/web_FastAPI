from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

import main

app = FastAPI()

@app.get("/")
async def root(request: Request):
    return main.templates.TemplateResponse('layout.html', context={'request': request})


templates = Jinja2Templates(directory="templates/")
