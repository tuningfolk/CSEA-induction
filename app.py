from flask import Flask, render_template, request
import urllib.request

import os
import requests
import urllib.parse

import countries
from countries import country

#Configuring application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True  

# Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")

@app.route('/', methods = ["GET", "POST"])
def index():
    if(request.method == "POST"):
        country_name = request.form.get("country_name")
        symbol = country_name
        url = f"https://api.weatherapi.com/v1/current.json?key=8e67619d356c4ac7ad861838230801&q={urllib.parse.quote(symbol)}&aqi=yes"

        response = requests.get(url)
        response.raise_for_status()

        quote = response.json()

            
    else:
        # api_key = os.environ.get("API_KEY")
        symbol = "NEW DELHI"
        url = f"https://api.weatherapi.com/v1/current.json?key=8e67619d356c4ac7ad861838230801&q={urllib.parse.quote(symbol)}&aqi=yes"

        response = requests.get(url)
        response.raise_for_status()

        quote = response.json()
        is_day = int(quote["current"]["is_day"])
        print(quote)



        return render_template("index.html", is_day = is_day, countries = country) 
    