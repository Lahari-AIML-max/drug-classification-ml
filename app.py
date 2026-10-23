
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Page settings
st.set_page_config(
    page_title="Drug Classification",
    page_icon="💊",
    layout="centered"
)

# Load the saved machine-learning model
MODEL_PATH = Path(__file__).parent / "drug_classification_pipeline.joblib"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


st.title("💊 Drug Classification App")
st.write(
    "Enter the details below to see the drug class "
    "predicted by our machine-learning model."
)

# Check that the saved model exists
if not MODEL_PATH.exists():
    st.error(
        "Model file not found. Make sure "
        "drug_classification_pipeline.joblib is in the project folder."
    )
    st.stop()

# Load the model and handle loading errors
try:
    model = load_model()
except Exception as e:
    st.error(f"Could not load the model: {e}")
    st.stop()

# Create the input form
with st.form("drug_input_form"):
    st.subheader("Enter patient details")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30,
        step=1
    )

    sex = st.selectbox(
        "Sex",
        options=["F", "M"]
    )

    bp = st.selectbox(
        "Blood Pressure",
        options=["LOW", "NORMAL", "HIGH"]
    )

    cholesterol = st.selectbox(
        "Cholesterol",
        options=["NORMAL", "HIGH"]
    )

    na_to_k = st.number_input(
        "Sodium-to-Potassium Ratio (Na_to_K)",
        min_value=1.0,
        max_value=50.0,
        value=15.0,
        step=0.1
    )

    submitted = st.form_submit_button("Predict Drug Class")

# Make a prediction when the button is pressed
if submitted:
    input_data = pd.DataFrame([{
        "Age": age,
        "Sex": sex,
        "BP": bp,
        "Cholesterol": cholesterol,
        "Na_to_K": na_to_k
    }])

    try:
        prediction = model.predict(input_data)[0]

        st.success(f"Predicted drug class: **{prediction}**")

        st.caption(
            "This prediction is for an academic machine-learning "
            "project only. It is not medical advice and must not "
            "be used to select or prescribe medication."
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")
