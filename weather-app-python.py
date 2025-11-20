import sys
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"  # JSON format
    response = requests.get(url)
    data = response.json()

    area = data["nearest_area"][0]["areaName"][0]["value"]
    region = data["nearest_area"][0]["region"][0]["value"]
    country = data["nearest_area"][0]["country"][0]["value"]
    temp = data["current_condition"][0]["temp_F"]
    desc = data["current_condition"][0]["weatherDesc"][0]["value"]

    return area, region, country, temp, desc

def main():
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
        sys.exit(1)

    city = " ".join(sys.argv[1:])
    area, region, country, temp, desc = get_weather(city)

    print(f"Weather for {area}, {region}, {country}:")
    print(f"Temperature: {temp}°F")
    print(f"Conditions:  {desc}")

if __name__ == "__main__":
    main()