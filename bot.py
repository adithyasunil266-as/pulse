city = "Kozhikode"
temp=28
print(f"Weather in {city} is {temp} degree celcius")

def greet(name):
    return f"Good morning,{name}"
print (greet("Adithya"))

data=[{"q":"The best time is now.","a":"Some author"}]
print(data[0]["q"])

try:
    result=risky_function()
    except Exception as e:
        print(f"something went wrong :{e}")

import requests
from datatime import date

def get_weather(city="Thiruvananthapuram"):
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3", timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"Weather unavailable ({e})"

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=10)
        response.raise_for_status()
        data=response.json()
        quote=data[0]["q"]
        author=data[0]["a"]
        return f"{quote} - {author}"
except Exception as e:
    return f"Quote unavailable ({e})"

def build_summary():
    today = date.today().strftime("%A, %d %B %Y")
    weather = get_weather()
    quote=get_quote()

    summary = f"""
PULSE - Daily Summary

{today}

WEATHER
{weather}
"""

TODAY'S QUOTE
{quote}

"""
    return summary

def run():
    summary = build_summary()
    print(summary)

    with open("daily_summary.txt","w",encoding="utf-8") as f:
        f.write(summary)
        print("Pulse ran successfully.")
    
if _name_=="_main_":
    run()    
