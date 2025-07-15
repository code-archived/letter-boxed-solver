from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from typing import List
# import requests

app = FastAPI()

# Serve static files from "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at root
@app.get("/")
def read_index():
    return FileResponse('index.html')

# Example puzzle data structure (to be fetched from GitHub or scraper)
# For a real app, fetch/update this from a repository or database.
from datetime import date
latest_puzzle = {
    "date": str(date.today()),
    "top": ["K","C","U"],
    "right": ["I","G","Q"],
    "bottom": ["N","E","W"],
    "left": ["S","J","A"]
}

@app.get("/api/puzzle")
def get_puzzle():
    # In production, you might fetch updated puzzle from GitHub repo here
    # e.g., using requests.get(raw_url) to fetch a JSON file with today's letters.
    return JSONResponse(content=latest_puzzle)

@app.get("/api/solve")
def solve_puzzle(words: int = 2):
    """
    words: number of words in solution (1,2, or 3).
    This function should implement the Letter Boxed solving logic. 
    Here, we'll mock it with a placeholder.
    """
    # In a real solver, fetch all valid words, build graph, find paths, etc.
    # For demonstration, we return a dummy solution.
    solutions = []
    # Example: pretend we found these solutions for 2-word request
    if words == 2:
        solutions = ["JUICES SQUAWKING"]
    elif words == 3:
        solutions = ["A WORD", "ANOTHER WAY"]
    elif words == 1:
        solutions = []  # likely no single-word solution
    return JSONResponse(content={"solutions": solutions})
