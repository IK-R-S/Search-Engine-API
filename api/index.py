from flask import Flask
from .engine import duckgo
import json

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Search engine API running", "engines online": {"name": "DuckGo", "endpoint": "/engines/duckgo/"}}

@app.route('/engines/duckgo/<q>')
def about(q):
    results = duckgo(query=q)
    response = json.dumps(results, ensure_ascii=False, indent=4)
    return response
