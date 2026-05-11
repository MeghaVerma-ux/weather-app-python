import tkinter as tk
import requests

# 🔑 Put your OpenWeather API key here
API_KEY = "9aa854d25c8af22550cf6ed9bd4d4c28"

# 🌤️ Function to get weather data
def get_weather():
    city = city_entry.get()

    if city.strip() == "":
        result_label.config(text="⚠️ Please enter a city name!")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            result_label.config(text="❌ City not found!")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        result_label.config(
            text=f"🌍 City: {city}\n"
                 f"🌡 Temperature: {temp}°C\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"☁ Condition: {weather}"
        )

    except:
        result_label.config(text="⚠️ Error fetching data!")

# 🪟 Main window
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.resizable(False, False)

# 🏷️ Title
title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# 📍 Input box
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

# 🔘 Button
get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_button.pack(pady=10)

# 📊 Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# 🚀 Run app
root.mainloop()