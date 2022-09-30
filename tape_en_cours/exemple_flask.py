from flask import Flask
import requests

app = Flask(__name__)


@app.route("/<path>")
def hello_world(path):
    return requests.get(f"https://api.github.com/{path}").json()
