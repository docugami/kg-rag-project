import os
import sys
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from langserve import add_routes
from docugami_kg_rag.chain import chain as docugami_kg_rag_chain
import subprocess

app = FastAPI()
templates = Jinja2Templates(directory="static/templates")

@app.get("/")
def root(request: Request):
    return RedirectResponse("/docugami-kg-rag/playground/earnings-call")

@app.get("/docugami-kg-rag/playground/earnings-call")
def playground(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

add_routes(app, docugami_kg_rag_chain, path="/docugami-kg-rag")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
