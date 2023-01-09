from flask import Flask, render_template, request, redirect
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
    # api_key = os.environ.get("API_KEY")
    symbol = "NEW DELHI"
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key=8e67619d356c4ac7ad861838230801&q={urllib.parse.quote(symbol)}&aqi=yes"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return redirect("/")


    
    try:
        quote = response.json()
    

        is_day = int(quote["current"]["is_day"])
        temp_c = quote["current"]["temp_c"]
        temp_f = quote["current"]["temp_f"]

        condition = quote["current"]["condition"]["text"]

        wind_kph = quote["current"]["wind_kph"]
        wind_degree = quote["current"]["wind_degree"]
        wind_dir = quote["current"]["wind_dir"]

        region = quote["location"]["name"]
        location_country = quote["location"]["country"]

    except (KeyError, TypeError, ValueError):
        return redirect("/")

    if(request.method == "POST"):
        country_name = request.form.get("country_name")
        symbol = country_name
        print(symbol)
        try:
            url = f"https://api.weatherapi.com/v1/current.json?key=8e67619d356c4ac7ad861838230801&q={urllib.parse.quote(symbol)}&aqi=yes"
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException:
            return redirect("/")


        
        try:
            quote = response.json()
        

            is_day = int(quote["current"]["is_day"])
            temp_c = quote["current"]["temp_c"]
            temp_f = quote["current"]["temp_f"]

            condition = quote["current"]["condition"]["text"]

            wind_kph = quote["current"]["wind_kph"]
            wind_degree = quote["current"]["wind_degree"]
            wind_dir = quote["current"]["wind_dir"]

            region = quote["location"]["name"]
            location_country = quote["location"]["country"]

        except (KeyError, TypeError, ValueError):
            return redirect("/")



    

    return render_template("index.html", condition = condition, wind_kph = wind_kph, wind_degree = wind_degree, wind_dir = wind_dir, is_day = is_day,temp_c = temp_c, temp_f = temp_f, region = region, location_country  = location_country, countries = country,)

    