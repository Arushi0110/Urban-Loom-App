import streamlit as st
def set_sidebar_bg_from_url(url):
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def set_page_bg_from_url(url):
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Set the background images for the entire app ---
# This URL will be used for the page background
page_bg_url = "https://img.freepik.com/free-vector/black-background-with-focus-spot-light_1017-27230.jpg?semt=ais_hybrid&w=740&q=80" 
set_page_bg_from_url(page_bg_url)

# This URL will be used for the sidebar background
sidebar_bg_url = "https://images.pexels.com/photos/1679719/pexels-photo-1679719.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
set_sidebar_bg_from_url(sidebar_bg_url)

st.set_page_config(page_title="Urban Loom", layout="wide")

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