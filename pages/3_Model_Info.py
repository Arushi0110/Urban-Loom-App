import streamlit as st
import pandas as pd


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