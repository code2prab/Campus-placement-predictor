import streamlit as st
import pandas as pd
import numpy as np
import pickle

file = open('campusplacementpredictor.pkl', 'rb')
rf = pickle.load(file)
file.close()

data = pd.read_csv('Placement_Data_Full_Class.csv')

st.title("Campus Placement Predictor")

Gender = st.selectbox('Gender', data['gender'].unique())

spec = st.selectbox('Specialisation', data['specialisation'].unique())

ssc_b = st.selectbox('SSC_board', data['ssc_b'].unique())

ssc_p = st.number_input('SSC percentage')

hsc_b = st.selectbox('HSC_board', data['hsc_b'].unique())

hsc_s = st.selectbox('HSC_Stream', data['hsc_s'].unique())

hsc_p = st.number_input('HSC percentage')

degree_stream = st.selectbox('degree_Stream', data['degree_t'].unique())

degree_p = st.number_input('Degree percentage')

mba_p = st.number_input('MBA Percentage')

workex = st.selectbox('Work_experience', data['workex'].unique())

if st.button('Predict Placement percentage'):

    
    if Gender == 'M':
        Gender = 1
    else:
        Gender = 0
        
    if spec == 'Mkt&HR':
        spec = 1
    else:
        spec = 0

    if ssc_b == 'Others':
        ssc_b = 1
    else:
        ssc_b = 0
        
    if hsc_b == 'Others':
        hsc_b = 1
    else:
        hsc_b = 0
        
    if hsc_s == 'Arts':
        hsc_s = 0
    elif hsc_s == 'Commerce':
        hsc_s = 1
    else:
        hsc_s = 2
        
    
    
    if degree_stream == 'Comm&Mgmt':
        degree_stream = 0
    elif degree_stream == 'Others':
        degree_stream = 1
    else:
        degree_stream = 2
        
    if workex == 'Yes':
        workex = 1
    else:
        workex = 0
        
    

    query = np.array([Gender,spec, degree_stream,workex,ssc_p,hsc_p,degree_p,mba_p])

    query = query.reshape(1, 8)

    prediction = rf.predict_proba(query)[0][1]

    st.title("Percentage of getting placed is " +
             str(prediction*100) + "%")
