city = "Kozhikode"
temp=28
print(f"Weather in {city} is {temp} degree celcius")

def greet(name):
    return f"Good morning,{name}"
print (greet("Adithya"))

data=[{"q":"The best time is now.","a":"Some author"}]
print(data[0]["q"])

def risky_function():
    try:
        return "Test successful"
    except Exception as e:
        return f"something went wrong :{e}"

import requests
from datetime import date

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

def get_tech_news():
    try:
        response = requests.get("https://hn.algolia.com/api/v1/search?tags=front_page", timeout=10)
        response.raise_for_status()
        data = response.json() 
        headline = data["hits"][0]["title"]
        return headline
    except Exception as e:
        return f"Tech news unavailable ({e})"       

def build_summary():
    today = date.today().strftime("%A, %d %B %Y")
    weather = get_weather()
    quote=get_quote()
    tech_news = get_tech_news()

    summary = f"""
PULSE - Daily Summary

{today}

WEATHER
{weather}

TODAY'S QUOTE
{quote}

TECH NEWS
{tech_news}

"""
    return summary

def run():
    summary = build_summary()
    print(summary)

    with open("daily_summary.txt","w",encoding="utf-8") as f:
        f.write(summary)
        print("Pulse ran successfully.")
    
if __name__=="__main__":
    run()
