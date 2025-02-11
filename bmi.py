import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time
st.title("WELCOME TO BMI CALCULATOR")
st.subheader("enter your weight in kg:")
w=st.number_input("enter your weight",min_value=5,max_value=250,value=10)
if w:
    st.write("your weight is",w)
st.subheader("enter your height:")
h=st.slider("select your height",10,210)
if h:
    st.write("your height is",h)
unit = st.selectbox('Select Units: ', ['cm','m','inches'])
if unit == 'cm':
 bmi = (w/((h/100)**2))
elif unit == 'm':
  bmi= (w/(h**2))
elif unit == 'inches':
  bmi = ((w)/(h**2))*703
st.write('Your BMI is', round(bmi, 2))
if (bmi<18.5):
 st.write('You are underweight,eat more and donot worry')
elif((bmi>=18.5) & (bmi<25)):
 st.write('You are healthy')
elif((bmi>=25) & (bmi<30)):
 st.write('You are overweight,but donot stress out')
else:
  st.write('you are obese please focus on your health')




