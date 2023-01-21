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
import plotly.express as px

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
    
   

    
    return round(float(prediction),2), report_data
 
def user_report(WinterRain, AGST, HarvestRain, Age, FrancePop):
    user_report_data = {
      'WinterRain':WinterRain,
      'AGST':AGST,
      'HarvestRain':HarvestRain,
      'Age':Age,
      'FrancePop':FrancePop,
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
return report_data
    
user_data = user_report()
st.header('Player Data')
st.write(user_data)
    


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
    if st.button("report_data"):
        data=user_report(WinterRain, AGST, HarvestRain, Age, FrancePop)
    st.success('Wine price for given input set is   : ${}'.format(result))
    #st.success('The output is -->  {}'(result))
    
    df = pd.read_csv("./wine.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
    # df = pd.read_excel(...)  # will work for Excel files

    if st.button("Show data"):
        st.title("Hello world!")  # add a title
        st.write(df)  # visualize my dataframe in the Streamlit app
     
    if st.button("Show graphs"):   
        fig = px.scatter(df,        
        x="WinterRain",
        y="Price",
        #size="pop",
        #color="continent",
        #hover_name="country",
        #log_x=True,
        #size_max=60,
        )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    