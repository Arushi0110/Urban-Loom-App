import streamlit as st


st.set_page_config(page_title="Urban Loom", layout="wide")

import pandas as pd

st.title("🏙️ :blue[Urban Loom: Traffic & Emissions Predictor]")

st.markdown("""
Welcome to :green[**Urban Loom**], a Machine Learning project that predicts :violet[**traffic density**] and :violet[**estimates CO₂ emissions**] in a futuristic city based on various urban factors.

This application is built with a machine learning model that analyzes key factors like weather, time of day, and vehicle types to provide accurate traffic predictions. It also includes a unique feature to demonstrate the environmental impact of transitioning to electric and autonomous vehicles.

### :red[Key Features:]
- :orange[**Traffic Prediction**:] Predict traffic density in real-time based on various urban conditions.
- :orange[**Data Visualization**:] Explore key patterns and relationships in the dataset used for training.
- :orange[**Model Information**:] Learn about the machine learning pipeline, including data preprocessing and model evaluation.
- :orange[**What-If Scenario**:] Explore a hypothetical future where a percentage of vehicles are electric and see the impact on CO₂ emissions.
- :orange[**Feedback**:] Provide your valuable thoughts and suggestions for the app.

### :green[⬅] :blue[Use the navigation bar on the left to explore the different sections of the app.]
""")