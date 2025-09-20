import streamlit as st
import joblib
import pandas as pd
import numpy as np

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

st.title(":blue[🚦Predict Traffic Density]")

# Get unique values for dropdowns
cities = ['SolarisVille', 'AquaCity', 'Neuroburg', 'Ecoopolis', 'MetropolisX', 'TechHaven']
vehicle_types = ['Drone', 'Flying Car', 'Autonomous Vehicle', 'Car']
weather_conditions = ['Snowy', 'Solar Flare', 'Clear', 'Rainy', 'Electromagnetic Storm']
economic_conditions = ['Stable', 'Recession', 'Booming']
days_of_week = ['Sunday', 'Wednesday', 'Saturday', 'Thursday', 'Monday', 'Friday', 'Tuesday']

# Create input widgets
col1, col2 = st.columns(2)
with col1:
    city = st.selectbox("City", cities)
    vehicle_type = st.selectbox("Vehicle Type", vehicle_types)
    weather = st.selectbox("Weather", weather_conditions)
    economic_condition = st.selectbox("Economic Condition", economic_conditions)
    energy_consumption = st.slider("Energy Consumption (kWh)", 0.0, 200.0, 50.0)

with col2:
    day_of_week = st.selectbox("Day of Week", days_of_week)
    hour_of_day = st.slider("Hour of Day", 0, 23, 12)
    speed = st.slider("Speed (km/h)", 0, 150, 60)
    is_peak_hour = st.checkbox("Is Peak Hour (7-9 AM & 4-6 PM)", value=False)
    random_event_occurred = st.checkbox("Random Event Occurred", value=False)

# Convert boolean checkboxes to integers
is_peak_hour_int = 1 if is_peak_hour else 0
random_event_occurred_int = 1 if random_event_occurred else 0

# --- Prediction and Display ---
if st.button(":green[Predict Traffic]"):
    # Create a DataFrame from the user's input
    input_data = pd.DataFrame([{
        'City': city,
        'Vehicle Type': vehicle_type,
        'Weather': weather,
        'Economic Condition': economic_condition,
        'Day Of Week': day_of_week,
        'Hour Of Day': hour_of_day,
        'Speed': speed,
        'Is Peak Hour': is_peak_hour_int,
        'Random Event Occurred': random_event_occurred_int,
        'Energy Consumption': energy_consumption
    }])

    # Make the prediction using the loaded pipeline
    predicted_traffic = pipeline.predict(input_data)[0]

    st.header(":green[Results]")
    st.markdown(f":orange[**Based on the provided conditions, the model predicts the following traffic information:**]")
    st.metric(label="Predicted Traffic Density", value=f"{predicted_traffic:.4f}")

    # Interpret the traffic density to give a simple text output
    if predicted_traffic > 70:
        st.warning("⚠️ **Traffic is expected to be heavy.**")
    elif predicted_traffic > 40:
        st.info("🚗 **Traffic is expected to be moderate.**")
    else:
        st.success("✅ **Traffic is expected to be light.**")

    # --- Emission Estimation ---
    def estimate_emissions(predicted_traffic, vehicle_type, avg_emission_per_vehicle_ice=0.23, avg_emission_per_vehicle_ev=0.05):
        if vehicle_type == 'Car':
            return predicted_traffic * avg_emission_per_vehicle_ice
        elif vehicle_type in ['Electric Car', 'Autonomous Vehicle', 'Flying Car', 'Drone']:
            return predicted_traffic * avg_emission_per_vehicle_ev
        else:
            return predicted_traffic * avg_emission_per_vehicle_ice

    estimated_emissions = estimate_emissions(predicted_traffic, vehicle_type)
    st.metric(label="Estimated CO₂ Emissions", value=f"{estimated_emissions:.2f} kg CO₂")
    st.info("💡 **Note:** The CO₂ emission values are simplified for demonstration purposes.")