# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:59:18 2022

@author: NiruSai
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import os



pickle_in=open("model.pkl","rb")
model=pickle.load(pickle_in)



def welcome():
    return "Welcome All"


def predict_stock(cylinders,displacement,horsepower,weight,acceleration,modelyear,origin):
    prediction=model.predict([[cylinders,displacement,horsepower,weight,acceleration,modelyear,origin]])
    print(prediction)
    return prediction


def main():
    """st.title( ")"""
    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">MPG Prediction Using Streamlit </h2>

    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    cylinders = st.text_input("cylinders")
    displacement = st.text_input("displacement")
    horsepower = st.text_input("horsepower")
    weight = st.text_input("weight")
    acceleration=st.text_input("acceleration")
    modelyear=st.text_input("model year")
    origin_list=['1','2','3']
    origin=st.selectbox("select the origin-  1:USA,  2: Europe , 3: Japan",origin_list)
    result=""
    if st.button("Predict"):
        result=predict_stock(cylinders,displacement,horsepower,weight,acceleration,modelyear,origin)
    st.success('The output is {}'.format(result))
    

     
    
if __name__=='__main__':
    main()
