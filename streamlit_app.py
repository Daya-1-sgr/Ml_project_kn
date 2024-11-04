import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline,CustomData
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



st.title('Hello there')

st.header('input features')
gender=st.selectbox('gender',('male','female'))
race_ethnicity=st.selectbox('race_ethnicity',('group B', 'group C', 'group A', 'group D', 'group E'))
parental_level_of_education=st.selectbox('Parental_level_of_education',("bachelor's degree", 'some college', "master's degree",
       "associate's degree", 'high school', 'some high school'))
lunch=st.selectbox('lunch',('standard', 'free/reduced'))
test_preparation_course=('test_preparation_course',('none', 'completed'))
reading_score=st.slider('reading score',10,100,68)
writing_score=st.slider('writing_score',17,100,69)

data={'gender':gender,'race_ethnicity':race_ethnicity,'parental_level_of_education':parental_level_of_education
      ,'lunch':lunch,'test_preparation_course':test_preparation_course,'reading_score':reading_score,'writing_score':writing_score}
input_dataframe=pd.DataFrame(data)

input_dataframe