import requests
import tkinter as tk
from tkinter import messagebox
from config import API_KEY

#API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_URL = "http://api.weatherapi.com/v1/current.json"



def get_weather_data(city):
    # Parameters for the API request
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    """
    params = {
        "key" : API_KEY,
        "q" : city
    }
    try:
        # Send GET request to the API
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an exception for unsuccessful requests
        data = response.json()
        
        # Extract relevant weather information from the response
        temperature = data["current"]["temp_c"] #data["main"]["temp"]
        humidity = data["current"]["humidity"]#data["main"]["humidity"]
        wind_speed = data["current"]["wind_kph"] #data["wind"]["speed"]

        # Display the weather information
        return {"temperature" :temperature,
                "humidity" : humidity,
                "wind_speed": wind_speed}

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        messagebox.showerror("error", "try again")


# GUI Application using Tkinter
class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Weather Forecast")
        self.geometry("300x150")

        self.city_entry = tk.Entry(self)
        self.city_entry.pack(pady=10)

        self.search_btn = tk.Button(self, text="Search", command=self.search_weather)
        self.search_btn.pack()
        
        self.temperature = tk.Label(text="Temperature: ")
        self.humidity = tk.Label(text="Humidity: ")
        self.wind_speed = tk.Label(text="Wind Speed: ")

        self.temperature.pack()
        self.humidity.pack()
        self.wind_speed.pack()

    def search_weather(self):
        city = self.city_entry.get()
        weather = get_weather_data(city)
        self.temperature["text"] = f"Temperature: {weather['temperature']}"
        self.humidity["text"] = f"Humidity: {weather['humidity']}"
        self.wind_speed["text"] = f"Wind Speed: {weather['wind_speed']}"


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()