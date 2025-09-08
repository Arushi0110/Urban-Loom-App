import streamlit as st
import joblib
import pandas as pd
import numpy as np

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

# --- Caching the model loading function ---
@st.cache_resource
def load_ml_pipeline():
    try:
        pipeline = joblib.load("traffic_prediction_pipeline.pkl")
        return pipeline
    except FileNotFoundError:
        st.error("Error: The 'traffic_prediction_pipeline.pkl' file was not found.")
        st.stop()

pipeline = load_ml_pipeline()

st.title(":blue[💡What-If Scenario: EV Adoption]")

st.markdown("""
### 🌳 :green[Environmental Impact]
Explore the potential reduction in CO₂ emissions if a percentage of vehicles in the city were to become electric. Use the slider below to see the impact.
""")

# --- What-If Scenario Calculation ---
ev_penetration_rate = st.slider("EV Penetration Rate (%)", 0, 100, 20, 5)
ev_penetration_rate /= 100.0  # Convert to a decimal

avg_emission_per_vehicle_ice = 0.23  # kg CO2/vehicle (simplified)
avg_emission_per_vehicle_ev = 0.05    # kg CO2/vehicle (simplified)

# Create a sample input to get a base prediction
sample_input = pd.DataFrame([{
    'City': 'SolarisVille',
    'Vehicle Type': 'Car',
    'Weather': 'Clear',
    'Economic Condition': 'Stable',
    'Day Of Week': 'Tuesday',
    'Hour Of Day': 12,
    'Speed': 60,
    'Is Peak Hour': 0,
    'Random Event Occurred': 0,
    'Energy Consumption': 50.0
}])

# Get a base traffic prediction
predicted_traffic = pipeline.predict(sample_input)[0]

# Calculate total emissions with 0% EVs (original)
original_emissions = predicted_traffic * avg_emission_per_vehicle_ice

# Calculate emissions in the what-if scenario
what_if_emissions = predicted_traffic * ((1 - ev_penetration_rate) * avg_emission_per_vehicle_ice + ev_penetration_rate * avg_emission_per_vehicle_ev)

# Calculate percentage reduction
if original_emissions > 0:
    reduction = ((original_emissions - what_if_emissions) / original_emissions) * 100
else:
    reduction = 0

st.markdown("---")
st.subheader(":orange[🏆 Results:]")

st.info(f"### 🚘The model predicts a traffic density of **{predicted_traffic:.2f}** for the sample conditions.")

st.metric(
    label="Original Estimated CO₂ Emissions 🏭",
    value=f"{original_emissions:.2f} kg CO₂"
)

st.metric(
    label=f"Emissions with {ev_penetration_rate*100:.0f}% EV Adoption ⚡️",
    value=f"{what_if_emissions:.2f} kg CO₂"
)

st.success(f"### 🎉 Significant Reduction Achieved!")
st.metric(
    label="Total Percentage Reduction✨",
    value=f"{reduction:.2f}%",
    delta=f"-{reduction:.2f}%",
    delta_color="normal"
)

st.warning("💡 **Note:** The emission values are estimates for a single point in time and are simplified for demonstration purposes.")