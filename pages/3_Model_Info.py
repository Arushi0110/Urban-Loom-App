import streamlit as st
import pandas as pd

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

st.title(":blue[🧠Model Information & Evaluation]")

st.markdown("""
### :violet[🔍 Machine Learning Pipeline]
This application uses a `RandomForestRegressor` model wrapped in a `scikit-learn` pipeline. The pipeline automates the data preprocessing steps to ensure consistency between training and prediction.

:red[**Pipeline Steps:**]
1.  :orange[**Preprocessing (`ColumnTransformer`)**:]
    -   `OneHotEncoder` for categorical features (`City`, `Weather`, etc.).
    -   `StandardScaler` for continuous numerical features (`Speed`, `Energy Consumption`, etc.).
    -   `passthrough` for binary features (`Is Peak Hour`, `Random Event Occurred`).
2.  :orange[**Regression (`RandomForestRegressor`)**:] The preprocessed data is fed into a Random Forest model to predict traffic density.
""")

st.markdown("---")

st.header("📈 :violet[Model Performance Comparison]")

st.info("The metrics below were obtained by evaluating both the `LinearRegression` and `RandomForestRegressor` models on the test set of the dataset.")

# Replace these values with the actual results from running your notebook
data = {
    'Model': ['Linear Regression', 'Random Forest Regressor'],
    'Mean Absolute Error (MAE)': [8.5714, 0.4907],
    'R-squared (R²) Score': [0.6510, 0.9997]
}

df_metrics = pd.DataFrame(data).set_index('Model')
st.table(df_metrics)

st.markdown("""
* :orange[**Mean Absolute Error (MAE)**:] Measures the average magnitude of the errors in a set of predictions, without considering their direction. A lower MAE indicates better performance.
* :orange[**R-squared (R²)**:] Represents the proportion of the variance for a dependent variable that's explained by an independent variable or variables in a regression model. A higher R² (closer to 1.0) indicates a better fit.""")

st.markdown("---")

st.warning ( "### 🏆 Based on these metrics, the :green[**Random Forest Regressor**] is the superior model for this task.")