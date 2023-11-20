import os
import sys
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from langserve import add_routes
from docugami_kg_rag.chain import chain as docugami_kg_rag_chain
import subprocess

app = FastAPI()

@app.get("/")
def root(request: Request):
    return RedirectResponse("/docugami-kg-rag/playground")

add_routes(app, docugami_kg_rag_chain, path="/docugami-kg-rag")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
