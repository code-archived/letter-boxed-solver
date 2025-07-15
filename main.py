# -*- encoding: utf-8 -*-

"""
Frontend Framework for the Letter Boxed Solver using FastAPI

Serve the data and solutions using the FastAPI framework and get the
data, solution hosted using ``uvicorn main:app`` from the server.
"""

import os
import sys

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

# append the root directory, get the absolute path and add to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

import src as lbsolver

# ! define the fastapi app, and register static directory for css, js
app = FastAPI()
app.mount("/static", StaticFiles(directory = "static"), name = "static")

# ! register the puzzle model, and get todays' data from scrapper
scrapper = lbsolver.ScrapeLetterBox()

@app.get("/")
def read_index():
    return FileResponse("index.html")


@app.get("/api/puzzle")
def get_puzzle():
    return JSONResponse(content = scrapper.getjson())

@app.get("/api/solve")
def solve_puzzle(words: int = 2) -> dict:
    model = lbsolver.LetterBoxedModel(
        boxes = scrapper.sides,
        words = scrapper.corpus
    )

    return JSONResponse(content = {
        "solutions" : model.solve(words)
    })
