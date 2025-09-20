import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Page configuration ---
st.set_page_config(page_title="📊 Traffic Data Visualization", layout="wide")



# --- Page title ---
st.title("📊 :blue[Traffic Data Visualization & Exploration]")

st.markdown("""
👋 :green[**Welcome!**]
This dashboard helps you :green[**understand traffic patterns**] in a futuristic city.  
We will explore how:
- 🚗 Vehicle :violet[**speed**] relates to :violet[**traffic congestion**] 
- 🌦️ :violet[**Weather**] affects traffic density  
- 📈 Traffic values are distributed across the dataset  

👉 Scroll down, select your options, and click :red[**Show Insights**] to see the charts.
""")

# --- Load Data ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("futuristic_city_traffic.csv")
        return df
    except FileNotFoundError:
        st.error("❌ The file 'futuristic_city_traffic.csv' was not found.")
        st.stop()

df = load_data()

# --- Dataset Preview ---
st.header("🔍 :green[Dataset Overview]")
st.write("Here’s a quick look at the dataset we are using.")
st.write("Shape of dataset (rows, columns):", df.shape)
st.dataframe(df.head())

# Separate numeric and categorical columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

st.markdown("---")

# --- User Inputs for Charts ---
st.header("📊 :blue[Select Options for Visualizations]")

st.subheader("🔵 :red[Scatter Plot Options]")
x_axis = st.selectbox("👉 Choose the first factor (X-axis)", numeric_cols, index=0, key="scatter_x")
y_axis = st.selectbox("👉 Choose the second factor (Y-axis)", numeric_cols, index=1, key="scatter_y")
hue_col = st.selectbox("🎨 Color the dots by (optional)", [None] + categorical_cols + numeric_cols, key="scatter_hue")

st.subheader("🟢 :red[Bar Chart Options]")
group_col = st.selectbox("👉 Choose a category (like Weather)", categorical_cols, key="bar_group")
target_col = st.selectbox("👉 Choose what to measure (numeric)", numeric_cols, key="bar_target")

st.subheader("🟣 :red[Histogram Options]")
hist_col = st.selectbox("👉 Choose a numeric column", numeric_cols, key="hist_col")
bins = st.slider("📏 Number of bins (grouping intervals)", min_value=5, max_value=100, value=30, key="hist_bins")

# --- Button to show charts ---
if st.button("📈 :green[Show Insights]"):

    st.markdown("---")
    # Scatter Plot
    st.header("🔵 :green[Scatter Plot: Compare Two Factors]")
    st.info("This chart compares **two numeric factors**. Each dot represents one data point.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=x_axis, y=y_axis, data=df, hue=hue_col, palette="viridis", ax=ax)
    ax.set_title(f"{x_axis} vs {y_axis}", fontsize=14, fontweight="bold")
    st.pyplot(fig)

    st.markdown(f"""
    :orange[**How to read this chart:** ] 
    - The :violet[**horizontal axis**] shows `{x_axis}`  
    - The :violet[**vertical axis**]shows `{y_axis}`  
    - Each dot is one observation  
    - If colored, dots are grouped by `{hue_col}`  
    """)

    st.markdown("---")
    # Bar Chart
    st.header("🟢 :green[Bar Chart: Compare Categories]")
    st.info("This chart compares the **average value** of a number across categories.")
    avg_values = df.groupby(group_col)[target_col].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=avg_values.index, y=avg_values.values, palette="viridis", ax=ax)
    ax.set_title(f"Average {target_col} by {group_col}", fontsize=14, fontweight="bold")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

    st.markdown(f"""
    :orange[**How to read this chart:** ] 
    - Each bar represents one `{group_col}` category  
    - The :violet[**height of the bar**] shows the :violet[**average**] `{target_col}`  
    """)

    st.markdown("---")
    # Histogram
    st.header("🟣 :green[Histogram: Distribution of Values]")
    st.info("This chart shows **how often different values occur**.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df[hist_col], bins=bins, kde=True, color="purple", ax=ax)
    ax.set_title(f"Distribution of {hist_col}", fontsize=14, fontweight="bold")
    st.pyplot(fig)

    st.markdown(f"""
    :orange[**How to read this chart:**]
    - Horizontal axis = `{hist_col}` values  
    - Vertical axis = frequency of those values  
    - Curve shows the overall trend  
    """)

    st.markdown("---")
    st.success("✅ Tip: Try changing the dropdowns above and click **Show Insights** again to explore more.")
