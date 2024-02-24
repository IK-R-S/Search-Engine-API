from flask import Flask
from .engine import duckgo
import json

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Search engine API running", "engines online": {"name": "DuckGo", "endpoint": "/engines/duckgo/"}}

@app.route('/engines/duckgo/<q>')
def duckgo(q):
    results, status_code = duckgo(query=q)
    return results, status_code
