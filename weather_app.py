import tkinter as tk
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
import os 
 

# city = input("Enter city: ")

# weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=imperial&APPID=abbdfafcb4c39610f07904ddd787fe33")

# print(weather_data.json())

load_dotenv()

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=imperial&appid="+os.environ.get('api_key')+""
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = json_data['main']['temp']
    feels_like = json_data['main']['feels_like']
    min_temp = json_data['main']['temp_min']
    max_temp = json_data['main']['temp_max']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    now = datetime.now()
    current_date = "Today is " + now.strftime("%m/%d/%Y")
    current_time = "The time is " + now.strftime("%I:%M:%S")
    final_info = condition + "\n" + str(temp) + "°F" 
    final_data = "\n"+ "Feels Like: " + str(feels_like) + "°F" + "\n"+ "Min Temp: " + str(min_temp) + "°F" + "\n" + "Max Temp: " + str(max_temp) + "°F" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "am" + "\n" + "Sunset: " + sunset + "pm"
    label1.config(text = current_date)
    label2.config(text = current_time)
    label3.config(text = final_info)
    label4.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=f)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
label3 = tk.Label(canvas, font=t)
label3.pack()
label4 = tk.Label(canvas, font=f)
label4.pack()
canvas.mainloop()