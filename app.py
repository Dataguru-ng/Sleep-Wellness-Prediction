import numpy as np
import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing


loaded_model = joblib.load('model.joblib2')

def prediction(data):
    sleep_df = pd.DataFrame(data)

    #sc = StandardScaler()

    num_data = sleep_df.values.reshape(1, -1)

    pred = loaded_model.predict(num_data)

    if pred[0] == 0 :
     return "User has Low or Normal Stress Level"
    elif pred[0] ==1:
     return "User has Medium Low Stress Level"
    elif pred[0] ==2:
     return " User has Medium Stress Level"
    elif pred[0] ==3:
     return "User has Medium High Stress Level"
    else:
     return "User has High Stress Level"

def main():
    st.title(" Stress Level Prediction In Sleep Patterns")
    snoring_rate = st.number_input("Rate or Intensity of Snoring During Sleep")
    respiration_rate = st.number_input("Number of Breaths Taken Per Minute During Sleep")
    body_temperature = st.number_input("Temperature of the User During Sleep")
    limb_movement = st.number_input("The Rate or Intensity of Limb Movement During Sleep")
    blood_oxygen = st.number_input("The Amount of Oxygen Present in the Blood During Sleep")
    eye_movement = st.number_input("The Eye Movement Activity During Sleep")
    sleeping_hours = st.number_input("Number of Hours Slept During a Particular Sleep Session")
    heart_rate = st.number_input("Number of Heartbeats Per Minute Sleep")

    stress_level  = ""

    if st.button("Result"):
          stress_level = prediction([snoring_rate, respiration_rate, body_temperature, limb_movement,
       blood_oxygen, eye_movement, sleeping_hours, heart_rate])
          


    st.success(stress_level)

if __name__ == "__main__":
     main()