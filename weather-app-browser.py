import streamlit as st
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


# Streamlit UI
st.title("🌦️ Simple Weather App")

city = st.text_input("Enter a city name:")

if city:
    try:
        area, region, country, temp, desc = get_weather(city)

        st.subheader(f"Weather for {area}, {region}, {country}")
        st.write(f"**Temperature:** {temp}°F")
        st.write(f"**Conditions:** {desc}")

    except Exception as e:
        st.error("Could not fetch weather. Check the city name or try again.")