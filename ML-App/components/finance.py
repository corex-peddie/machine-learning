# Financial Analysis

import streamlit as st
import pandas as pd
import plotly.express as px
from joblib import load
import time

def app():
    st.title('Financial Analysis')

    st.write("Use our custom-built Machine Learning models and external algorithms to analyze the `financial performance` of your E-Commerce business ")

    data = pd.read_csv('ML-App/Data/finance.csv')
    data = data.drop(columns='Unnamed: 0')

    section = st.radio('Sections',('View your Data', 'Use the ML Models (Linear Regression)'))
    if section == 'View your Data':
        fig1 = px.line(data, x='Month Name', y=['Total Sales/Revenue', 'Expenses', 'Profit'], title='Your Business Data Summary', labels={'value': 'Money In/Out', 'Month Name': 'Month', 'variable': 'Legend'})
        st.plotly_chart(fig1)
        info = data[['Month Name', 'Month Number', 'Total Sales/Revenue', 'Expenses', 'Profit']]
        info = info.rename(columns={'Month Name': 'Month'})
        st.write(info)
    else:
        st.write('### Predict Future Revenue and Profits')
        forecast_profit = load('ML-App/Data/profit_forecast.joblib')
        forecast_expenses = load('ML-App/Data/expenses_forecasting.joblib')
        months = st.selectbox('Select a Future Month', ['Sept 2021', 'Oct 2021', 'Nov 2021', 'Dec 2021', 'Jan 2022', 'Feb 2022', 
        'Mar 2022', 'Apr 2022', 'May 2022', 'June 2022', 'July 2022', 'Aug 2022'])
        months_list = ['Sept 2021', 'Oct 2021', 'Nov 2021', 'Dec 2021', 'Jan 2022', 'Feb 2022', 
        'Mar 2022', 'Apr 2022', 'May 2022', 'June 2022', 'July 2022', 'Aug 2022']
        
        nums = []
        for i in range(21,33):
            nums.append(i)
        
        input1 = nums[months_list.index(months)]
        profits =  '$' + str(int(forecast_profit.predict([[input1]])[0][0]))
        expenses =  '$' + str(int(forecast_expenses.predict([[input1]])[0][0]))
        revenue = '$' + str(int(forecast_profit.predict([[input1]])[0][0] + forecast_expenses.predict([[input1]])[0][0]))
        with st.empty():
            for i in range(1):
                st.caption('Evaluating...')
                time.sleep(1)
            st.caption('Done!')
        st.write("AI's Predicted Revenue: " + f'`{revenue}`')
        st.write("AI's Predicted Expenses: " + f'`{expenses}`')
        st.write("AI's Predicted Profits: " + f'`{profits}`')
        st.write('----')
