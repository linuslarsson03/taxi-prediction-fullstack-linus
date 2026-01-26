import streamlit as st
import requests


API_BASE_URL = "http://localhost:8000"
PREDICT_ENDPOINT = "/api/taxi/predict"


st.title("Taxi price predictor")

distance = st.number_input("Distance (km)", 0.1, 150.0, 5.0)
duration = st.number_input("Duration (minutes)", 0.1, 200.0, 15.0)
day = st.selectbox("Day of week", ["Weekday", "Weekend"])
traffic = st.selectbox("Traffic", ["Low", "Medium", "High"])
weather = st.selectbox("Weather", ["Clear", "Rain", "Snow"])



if st.button("Predict"):
    trip_input = {
        "Trip_Distance_km": distance,
        "Trip_Duration_Minutes": duration,
        "Day_of_Week": day,
        "Traffic_Conditions": traffic,
        "Weather": weather
    }

    response = requests.post(
        API_BASE_URL + PREDICT_ENDPOINT,
        json=trip_input
    )

    st.write("Predicted price:", response.json()["predicted_price"])
