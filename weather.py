import requests
import json

API_KEY = "655ae81b4882e8e9d209cb48d2f7310b"    # Insert your API_KEY here!

city = input("Enter city: ").strip()

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={API_KEY}&units=metric&lang=ru"
)


response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Extracting the required information
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    print(f"🌤️ In {city} currently {temp}°C, {desc}")

    # Saving JSON
    filename = f"weather_{city.lower()}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Response saved in {filename}")
else:
    print(f"❌ Error:", response.status_code)
    print(response.text)