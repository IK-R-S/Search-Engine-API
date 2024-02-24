from flask import Flask
from .engine import duckgo
import json

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Search engine API running", "engines online": {"DuckGo": {"endpoint": "/engines/duckgo/"}}, "status code": 200} 200

@app.route('/engines')
def engines():
    return {"search engines": {"DuckGo": {"server": "https://duckduckgo.com/", "service status": "online"}, "Google": {"server": "https://google.com/", "service status": "offline"}}, "status code": 200}, 200

@app.route('/engines/duckgo')
def duckgo_info():
    return {"search engine": "DuckGo", "server": "https://duckduckgo.com/", "service status": "online", "status code": 200}, 200
    
@app.route('/engines/duckgo/<q>')
def duckgo_engine(q):
    results, status_code = duckgo(query=q)
    return results, status_code
    
@app.route('/engines/google')
def google_info():
    return {"search engine": "Google", "server": "https://google.com/", "service status": "offline", "status code": 503}, 503

@app.route('/engines/google/<q>')
def google_engine(q):
    return {"message": "engine unavailable", "service status": "offline", "status code": 503}, 503
