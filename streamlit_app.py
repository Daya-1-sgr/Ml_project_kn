import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


st.title('Math Score Predictor')


st.header('Please input the following details:')


gender = st.selectbox('Gender', ('male', 'female'))
race_ethnicity = st.selectbox('Race/Ethnicity', ('group B', 'group C', 'group A', 'group D', 'group E'))
parental_level_of_education = st.selectbox(
    'Parental Level of Education', 
    ("bachelor's degree", 'some college', "master's degree", "associate's degree", 'high school', 'some high school')
)
lunch = st.selectbox('Lunch', ('standard', 'free/reduced'))
test_preparation_course = st.selectbox('Test Preparation Course', ('none', 'completed'))
reading_score = st.slider('Reading Score', 10, 100, 68)
writing_score = st.slider('Writing Score', 10, 100, 69)

# Create a CustomData instance using the inputs
data = CustomData(
    gender=gender,
    race_ethnicity=race_ethnicity,
    parental_level_of_education=parental_level_of_education,
    lunch=lunch,
    test_preparation_course=test_preparation_course,
    writing_score=writing_score,
    reading_score=reading_score
)

# Convert the data into a DataFrame for prediction
input_dataframe = data.get_data_as_frame()

# Display the input data as a table for reference
st.subheader('Input Data:')
st.write(input_dataframe)

if st.button('Make Prediction'):
    # Make prediction using the pipeline
    prediction = PredictPipeline()
    preds = prediction.predict(input_dataframe)
    
    # Display the prediction result
    st.subheader('Prediction Result:')
    st.write(f'The Maths Score is: {preds[0]}')
