# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:17:50 2022

@author: Dwij
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open(r'D:\Disease Prediction\diabetes_model.sav','rb'))

heart_model = pickle.load(open(r'D:\Disease Prediction\heart_model.sav','rb'))

kidney_model = pickle.load(open(r'D:\Disease Prediction\kidney_model.sav','rb'))


breast_cancer_model = pickle.load(open(r'D:\Disease Prediction\breast_cancer_model (2).sav','rb'))


#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',['Heart Disease Prediction','Diabetes Prediction','Breast Cancer Prediction','Kidney Disease Prediction'],default_index = 0)
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
    
# Breast Cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        meantexture = st.text_input('Mean Texture')
        
    with col2:
        meansmoothness = st.text_input('Mean Smoothness')
        
    with col3:
        meancompactness = st.text_input('Mean Compactness')
        
    with col1:
        meanconcavity = st.text_input('Mean Concavity')
        
    with col2:
        areaerror = st.text_input('Area Error')
        
    with col3:
        compactnesserror = st.text_input('Compactness Error')
        
    with col1:
        symmetryerror = st.text_input('Symmetry Error')
        
    with col2:
        fractaldimensionerror = st.text_input('Fractional Dimension Error')
        
    with col3:
        worstradius = st.text_input('Worst Radius')
        
    with col1:
        worsttexture = st.text_input('Worst Texture')
        
    with col2:
        worstperimeter = st.text_input('Worst Perimeter')
        
    with col3:
        worstarea = st.text_input('Worst Area')
        
    with col1:
        worstconcavity = st.text_input('Worst Concavity')
        
    with col2:
        worstconcavepoints = st.text_input('Worst Concave Points')
            
    with col3:
        worstsymmetry = st.text_input('Worst Symmetry')
    
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        heart_prediction = breast_cancer_model.predict([[meantexture,meansmoothness,meancompactness,meanconcavity,areaerror,compactnesserror,symmetryerror,fractaldimensionerror,worstradius,worsttexture,worstperimeter,worstarea,worstconcavity,worstconcavepoints,worstsymmetry]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having breast cancer'
        else:
          heart_diagnosis = 'The person does not have any breast cancer'
        
    st.success(heart_diagnosis)
    
    
# Kidney Disease Prediction Page
if (selected == 'Kidney Disease Prediction'):
    
    # page title
    st.title('Kidney Disease Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        sg = st.text_input('SG')
        
    with col2:
        al = st.text_input('AL')
    
    with col3:
        sc = st.text_input('SC')
    
    with col1:
        hemo = st.text_input('HEMO')
    
    with col2:
        pcv = st.text_input('PCV')
    
    with col3:
        htn = st.text_input('HTN')
    
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Kidney Disease Test Result'):
        diab_prediction = kidney_model.predict([[sg,al,sc,hemo,pcv,htn]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person have kidney disease'
        else:
          diab_diagnosis = 'The person does not have kidney disease'
        
    st.success(diab_diagnosis)
