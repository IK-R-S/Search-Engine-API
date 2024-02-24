from flask import Flask
from .engine import duckgo

app = Flask(__name__)

print(resultados_json)
@app.route('/')
def home():
    return {"message": "Search engine API running", "engines online": {"name": "DuckGo", "endpoint": "/engines/duckgo/"}}

@app.route('/engines/duckgo/<q>')
def about(q):
    results = duckgo(query=q)
    response = json.dumps(results, ensure_ascii=False, indent=4)
    return response
