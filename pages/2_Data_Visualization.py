import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Page configuration
st.set_page_config(page_title="📊 Data Visualization", layout="wide")
st.title("📊 :blue[Data Visualization & EDA]")

st.markdown("""
This page provides an interactive look into the :green[]`futuristic_city_traffic.csv` dataset], offering insights into the relationships between features like speed, traffic density, and weather conditions.
""")

# Load data with caching to prevent reloading every time
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("futuristic_city_traffic.csv")
        return df
    except FileNotFoundError:
        st.error("Error: The file 'futuristic_city_traffic.csv' was not found.")
        st.stop()

df = load_data()

st.markdown("---")
st.subheader(":orange[Dataset Overview]")
st.write(df.head())

st.markdown("---")

# Plot 1: Scatter plot of Speed vs. Traffic Density
st.subheader(":red[Speed vs. Traffic Density]")
st.info("This scatter plot visualizes the relationship between vehicle speed and traffic density. Observe how traffic density changes as speed varies.")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Speed', y='Traffic Density', hue='Traffic Density', data=df, palette='viridis', ax=ax)
ax.set_title(":red[Relationship between Speed and Traffic Density")
st.pyplot(fig)

st.markdown("---")

# Plot 2: Bar chart of average Traffic Density by Weather Condition
st.subheader(":red[Average Traffic Density by Weather Condition]")
st.info("This bar chart shows the average traffic density for different weather conditions. You can see which weather types tend to have higher traffic.")
avg_traffic_by_weather = df.groupby('Weather')['Traffic Density'].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_traffic_by_weather.index, y=avg_traffic_by_weather.values, palette='viridis', ax=ax)
ax.set_title("Average Traffic Density by Weather")
ax.set_xlabel("Weather Condition")
ax.set_ylabel("Average Traffic Density")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

# Plot 3: Distribution of Traffic Density
st.subheader(":red[Distribution of Traffic Density]")
st.info("This histogram shows the frequency distribution of traffic density values across the entire dataset.")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df['Traffic Density'], bins=30, kde=True, color='purple', ax=ax)
ax.set_title("Distribution of Traffic Density")
ax.set_xlabel("Traffic Density")
ax.set_ylabel("Frequency")
st.pyplot(fig)