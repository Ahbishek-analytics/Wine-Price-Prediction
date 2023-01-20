# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 02:20:31 2023

@author: Abhishek Tiwari
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 02:20:31 2023

@author: Abhishek Tiwari
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("wine.pkl","rb")
wine=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(WinterRain, AGST, HarvestRain, Age, FrancePop):

    input=np.array([[WinterRain, AGST, HarvestRain, Age, FrancePop]]).astype(np.float64)
   
    prediction=wine.predict(input)
    #prediction=wine.predict([[WinterRain, AGST, HarvestRain, Age, FrancePop]])
    print("Wine Price prediction:")
    
    user_report_data = {
      'WinterRain':WinterRain,
      'AGST':AGST,
      'HarvestRain':HarvestRain,
      'Age':Age,
      'FrancePop':FrancePop,

    }
    report_data = pd.DataFrame(user_report_data, index=[0])

    
    
    
    return round(float(prediction),3), report_data
    
st.write(report_data)


def main():
    st.title("Wine Price Prediction")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Wine Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    WinterRain = st.text_input("WinterRain","Type Here")
    AGST = st.text_input("AGST","Type Here")
    HarvestRain = st.text_input("HarvestRain","Type Here")
    Age = st.text_input("Age","Type Here")
    FrancePop = st.text_input("FrancePop","Type Here")
    
    
    
    
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(WinterRain, AGST, HarvestRain, Age, FrancePop)

    st.success('Wine price for given input set is   : ${}'.format(result))
    #st.success('The output is -->  {}'(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    