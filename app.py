import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import GridSearchCV



linear = joblib.load('ad_Linear.joblib')
decisionT = joblib.load('ad_Decision.joblib')
randomF = joblib.load('ad_Random.joblib')
knear = joblib.load('ad_Knear.joblib')

Models = {
    'linear' : linear,
    'DecisionTree':decisionT,
    'RandomForest':randomF,
    'KNearestNeighbor':knear
}


# UI
st.title("Admission Prediction")

# Sidebar
st.sidebar.title("Predict Admission Probability")
gre = st.sidebar.slider("GRE Score", min_value=0, max_value=340, step=1, value=300)
toefl = st.sidebar.slider("TOEFL Score", min_value=0, max_value=120, step=1, value=100)
lor = st.sidebar.slider("LOR", min_value=1.0, max_value=5.0, step=0.1, value=3.0)
cgpa = st.sidebar.slider("CGPA", min_value=0.0, max_value=10.0, step=0.1, value=7.5)
sop = st.sidebar.slider("SOP", min_value=1.0, max_value=5.0, step=0.1, value=3.0)
research = st.sidebar.selectbox("Research Experience", ['Yes', 'No'])
university_rating = st.sidebar.slider("University Rating", min_value=1, max_value=5, step=1, value=3)

model_options = ['linear','DecisionTree','RandomForest','KNearestNeighbor']
selected_model = st.sidebar.selectbox("Select Model", model_options)

# Convert Research Experience to binary
research_binary = 1 if research == 'Yes' else 0

# Scale input features
input_features = [[gre, toefl, lor, cgpa, sop, research_binary, university_rating]]

# Prediction
predicted_probability = Models[selected_model].predict(input_features)[0]*100

# Display Prediction
st.subheader("Predicted Probability of Admission")
st.write(f"Using {selected_model}: {predicted_probability}")

