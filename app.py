import streamlit as st
import requests

st.title("🌦️ Weather App")

city = st.text_input("Enter city name")

if st.button("Get Weather"):
    response = requests.post("http://127.0.0.1:8000/aymen", json={"city": city})
    if response.status_code == 200:
        data = response.json()
        st.success(f"City: {data['city']}")
        st.info(f"Temperature: {data['temperature']} °C")
        st.write(f"Description: {data['description']}")
    else:
        st.error("City not found or API error.")
