import streamlit as st
import pandas as pd
import plotly.express as px
from joblib import load

def app():
    
    st.title('Website Analysis')
    st.write("Use our custom-built Machine Learning models to analyze your E-Commerce `website` and inspect its performance")

    section = st.radio('Sections',('View your Data', 'Use the ML Model (R.ForestRegressor)'))
    if section == 'View your Data':
        data = pd.read_csv('ML-App/Data/visitors.csv')
        data_avg = pd.read_csv('ML-App/Data/visitors_mean.csv')
        data = data.drop(columns='Unnamed: 0')
        fig1 = px.line(data,x='Date', y=['Total Visits' ,'Unique Visits' ,'First Time Visits' ,'Returning Visits'], labels={'value': 'Visits', 'variable': 'Legend', 'Date': 'Time (Increasing)'}, title='Visits over Time').update_xaxes(showticklabels=False)
        st.plotly_chart(fig1)
        fig2 = px.bar(data_avg, barmode='group', x='Day',  y=['Total Visits' ,'Unique Visits' ,'First Time Visits' ,'Returning Visits'], title='Average Visits per Day', labels={'value': 'Visits', 'variable': 'Legend'})
        st.plotly_chart(fig2)
    else:
        lr = load('ML-App/Data/rf_visitors.joblib')
        st.caption("This Week's Data:")
        col1, col2 = st.beta_columns([1,1])
        with col1:
            total_visits = st.number_input('Total Website Visits', 710)
            unique_visits = st.number_input('Unique Website Visits', 500)
        with col2:
            new_users = st.number_input('New Website Users', 454)
            return_users = st.number_input('Returning Website Users', 250)
        if st.button('Forecast New Measurements'):
            pred = lr.predict([[unique_visits, total_visits]])[0]
            st.write('### AI Prediction')
            st.write('New Users (next week):', int(pred[0]))
            st.write('Returning Users (next week):', int(pred[1]))





