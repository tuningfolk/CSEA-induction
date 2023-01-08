from flask import Flask, render_template
import urllib.request

import os
import requests
import urllib.parse

#Configuring application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True  

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.route('/')
def index():
    api_key = os.environ.get("API_KEY")
    symbol = "INDIA"
    url = f"https://api.weatherapi.com/v1/current.json?key='8e67619d356c4ac7ad861838230801'&q={urllib.parse.quote(symbol)}&aqi=yes"

    response = requests.get(url)
    response.raise_for_status()

    quote = response.json()
    # print(quote["location"]["name"])



    return render_template("index.html")    