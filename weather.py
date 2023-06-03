import urllib.request
import json

API_KEY = "602af398dbce5de3b039dacf9dc3ea68" 

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            main = data["weather"][0]["main"]
            description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            print(f"Weather forecast for {city}:")
            print(f"Main: {main}")
            print(f"Description: {description}")
            print(f"Temperature: {temperature} K")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
    except urllib.error.URLError:
        print("Failed to fetch weather data.")

if __name__ == "_main_":
    city = input(str("Enter city:")) 
    get_weather(city)
