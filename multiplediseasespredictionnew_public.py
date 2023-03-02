# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:06:05 2022

@author: Priya
"""
import pickle
import streamlit as st

from streamlit_option_menu import option_menu

heart_disease_model=pickle.load(open('D:Multiple Diseases Prection/heart_disease_prediction_model.sav','rb'))
diabetes_disease_model=pickle.load(open('D:Multiple Diseases Prection/diabetes_model2.sav','rb'))
breastcancer_model=pickle.load(open('D:Multiple Diseases Prection/breastcancer_model.sav','rb'))
#sidebar for navigation
with st.sidebar:
    selected=option_menu('Multiple Diseases Prediction',
                         ['Heart Diseases','Diabetes Prediction','Breast Cancer'],
                         icons = ['heart','activity','person'],
                         default_index=0)


#heart disease prediction
       
if (selected == "Heart Diseases"):
   st.title("Heart Diseases Prediction using ML") 
   col1,col2,col3 =st.columns(3)
   with col1:
       age=st.text_input("Age of a person")
   with col2:
       sex=st.text_input("Sex (0-female,1-male)")
   with col3:
       cp=st.text_input("Chestpain Type")
   with col1:
       trestbps = st.text_input("Resting Blood Pressure")
   with col2:
       chol=st.text_input("Serum Cholestroral in mg/dl")
   with col3:
       fbs=st.text_input("fasting Blood Sugar is greater than 120mg/dl (1-true,0-false)")
   with col1:
       restecg=st.text_input("Resting Electrocardiagraphic results")
   with col2:
       thalach=st.text_input("Maximum Heart Rate Achieved")
   with col3:
       exang=st.text_input("Exercise Induced Angina (1-yes,0-no)")
   with col1:
       oldpeak=st.text_input("ST depression included by exercise")
   with col2:
       slope=st.text_input("Slope of the peak exercise St segment")
   with col3:
       ca=st.text_input("Major vessels colored by flourosopy")
   with col1:
      thal=st.text_input("thal:0=normal;1=fixed defect;2=reversable defect")    
     
   heartd_dianosis = ''
   if st.button('Disease Test Result'):
       heart_prediction=heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
       if(heart_prediction[0]==1):
           heartd_dianosis='This person is having heart disease 😷'
           st.write("get well soon !!!!!")
       else:
           heartd_dianosis="not having heart disease"
           st.balloons()
   st.success(heartd_dianosis)        

         
#diabetes prediction

if (selected == "Diabetes Prediction"):
    st.title("Diabetes Prediction using ML")
    col1,col2,col3 =st.columns(3)
    with col1:
        Pregnancies=st.text_input("Num of pregnancies")
    with col2:
        Glucose=st.text_input("Glucose Level")
    with col3:
        BloodPressure=st.text_input("Blood Pressure value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness value")
    with col2:
        Insulin=st.text_input("Insulin level")
    with col3:
        BMI=st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Diabetes pedigree fun val")
    with col2:
        Age=st.text_input("Age of the person")      

    diabetes_prediction = ''
    if st.button('Disease Test Result'):
        diabetes_predictions=diabetes_disease_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(diabetes_predictions[0]==1):
            diabetes_prediction='This person is having diabetes 😷'
            st.write("get well soon !!!!!")
        else:
            diabetes_prediction='not having heart disease'
            st.balloons()
    st.success(diabetes_prediction)

## Breast cancer prediction
    
if (selected == "Breast Cancer"):
   st.title("Breast Cancer Prediction using ML")
   col1,col2,col3 =st.columns(3)
   with col1:
       mean_radius=st.text_input("Mean_Radius")
   with col2:
       mean_texture=st.text_input("Mean_Texture")
   with col3:
       mean_perimeter=st.text_input("Mean_Perimeter")
   with col1:
       mean_area=st.text_input("Mean_Area")
   with col2:
       mean_smoothness=st.text_input("Mean_Smoothness")    
       
   breastcancer_diagonsis = ''
   if st.button("Disease Test Result"):
       breastcancer_prediction=breastcancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness]])
       if(breastcancer_prediction[0]==1):
           breastcancer_diagonsis='This person is having the symtoms of breast cancer 😷'
           st.write("get well soon !!!!!")
       else:
           breastcancer_diagonsis='not having breast cancer disease'
           st.balloons()
   st.success(breastcancer_diagonsis)    
       