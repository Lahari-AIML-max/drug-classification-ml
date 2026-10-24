# drug-classification-ml

## Project Overview
This project compares machine learning algorithms to classify drug categories using patient attributes from the Drug200 dataset. It is an educational machine learning project and is not intended for clinical prescribing decisions.

## Dataset Features
- Age
- Sex
- Blood Pressure (BP)
- Cholesterol
- Na_to_K ratio

**Target:** Drug class

## Models Compared
Six classifiers were evaluated:
1. Logistic Regression
2. Random Forest
3. Gradient Boosting
4. Support Vector Machine (SVM)
5. XGBoost
6. LightGBM

## Preliminary Model Comparison

| Model | Test Accuracy | Macro F1 |
|---|---:|---:|
| LightGBM | 0.975 | 0.9492 |
| Logistic Regression | 0.975 | 0.9418 |
| Random Forest | 0.975 | 0.9418 |
| XGBoost | 0.925 | 0.8490 |
| Gradient Boosting | 0.925 | 0.8252 |
| SVM | 0.675 | 0.3046 |

These are preliminary results from a small dataset. Performance should not be interpreted as evidence of clinical reliability.

## Why Random Forest Was Selected

Random Forest was selected as our initial final model because it achieved strong performance on the held-out test set, with 97.5% accuracy and a macro F1-score of 0.9418. It supports multiclass classification and can learn complex, nonlinear relationships between patient attributes and drug classes.

Hyperparameter tuning was performed using stratified cross-validation. The selected model achieved a cross-validation macro F1-score of 1.0000 in the tested folds. The complete preprocessing and Random Forest pipeline was saved for integration into the Streamlit application.

LightGBM achieved a slightly higher macro F1-score in the preliminary baseline comparison. Therefore, Random Forest is our selected candidate based on the current experiments, not a proven universal winner. Further consistent validation is required because the Drug200 dataset contains only 200 records.

This project is intended for academic demonstration only and must not be used to make medical or prescribing decisions.

## Running the Web App

This project includes a Streamlit web app that uses the
saved machine-learning pipeline to predict a drug class
from the entered features.

### Requirements
- Python 3
- Dependencies listed in `requirements.txt`

### Setup

Create a virtual environment:

`python3 -m venv .venv`

Activate it on macOS or Linux:

`source .venv/bin/activate`

Install the dependencies:

`python -m pip install -r requirements.txt`

### Run the app

`streamlit run app.py`

Open the local URL shown in the terminal.

### Disclaimer

This application is for academic demonstration only.
Its predictions are not medical advice and must not be
used to select or prescribe medication.
