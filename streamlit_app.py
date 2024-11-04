import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline,CustomData
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



st.title('Hello there')

st.header('input features')
gender=st.selectbox('gender',('male','female'))
#race_ethnicity=st.selectbox('race_ethnicity',(''))