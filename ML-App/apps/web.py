import streamlit as st
import pandas as pd
import plotly.express as px
from joblib import load

def app():
    
    st.title('Website Analysis')
    st.write("Use our trained Artificial Intelligence models to analyze your E-Commerce `website`")

    section = st.radio('Select',('Visualize Data', 'Load the AI'))
    if section == 'Visualize Data':
        data = pd.read_csv('ML-App/Data/visitors.csv')
        data_avg = pd.read_csv('ML-App/Data/visitors_mean.csv')
        data = data.drop(columns='Unnamed: 0')
        fig1 = px.line(data,x='Date', y=['Total Visits' ,'Unique Visits' ,'First Time Visits' ,'Returning Visits'], labels={'value': 'Visits', 'variable': 'Legend', 'Date': 'Time (Increasing)'}, title='Visits over Time').update_xaxes(showticklabels=False)
        st.plotly_chart(fig1)
        fig2 = px.bar(data_avg, barmode='group', x='Day',  y=['Total Visits' ,'Unique Visits' ,'First Time Visits' ,'Returning Visits'], title='Average Visits per Day', labels={'value': 'Visits', 'variable': 'Legend'})
        st.plotly_chart(fig2)
    else:
        lr = load('ML-App/Data/lr_visitors.joblib')
        st.write('Model:', lr)




