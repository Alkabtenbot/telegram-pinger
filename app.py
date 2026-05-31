from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Pinger is alive"

@app.route('/ping')
def ping():
    replit_url = os.environ.get("REPLIT_URL")
    if replit_url:
        try:
            requests.get(replit_url, timeout=10)
        except:
            pass
    return "Pinged Replit"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
