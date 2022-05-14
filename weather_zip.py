import requests
from dotenv import load_dotenv
import os 

load_dotenv()

user_input = input("Enter zipcode: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?zip={user_input}&units=imperial&APPID={os.environ.get('api_key')}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['description'].capitalize()
    temp = round(weather_data.json()['main']['temp'])
    feels_like = round(weather_data.json()['main']['feels_like'])

    print(f"Today in {user_input} expect {weather} with a temperature of {temp}ºF.")
    print(f"It will feel like {feels_like}ºF.")
 