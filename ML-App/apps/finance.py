import streamlit as st
import pandas as pd
import plotly.express as px
from joblib import load

def app():
    st.title('Financial Ratings')

    st.write("Use our custom-built Machine Learning models and external algorithms to analyze the `financial performance` of your E-Commerce business ")

    data = pd.read_csv('ML-App/Data/finance.csv')
    data = data.drop(columns='Unnamed: 0')

    section = st.radio('Sections',('View your Data', 'Use the ML Models'))
    if section == 'View your Data':
        fig1 = px.line(data, x='Month Name', y=['Total Sales/Revenue', 'Expenses', 'Profit'], title='Your Data Summary', labels={'value': 'Money In/Out', 'Month Name': 'Month', 'variable': 'Legend'})
        st.plotly_chart(fig1)
        st.write(data)
    else:
        st.write('### Forecast Profits')
        forecast_profit = load('ML-App/Data/profit_forecast.joblib')
        months = st.selectbox('Select a Future Month', ['Sept 2021', 'Oct 2021', 'Nov 2021', 'Dec 2021', 'Jan 2022', 'Feb 2022', 
        'Mar 2022', 'Apr 2022', 'May 2022', 'June 2022', 'July 2022', 'Aug 2022'])
        months_list = ['Sept 2021', 'Oct 2021', 'Nov 2021', 'Dec 2021', 'Jan 2022', 'Feb 2022', 
        'Mar 2022', 'Apr 2022', 'May 2022', 'June 2022', 'July 2022', 'Aug 2022']
        
        nums = []
        for i in range(21,33):
            nums.append(i)
        
        input1 = nums[months_list.index(months)]
        output1 =  '$' + str(int(forecast_profit.predict([[input1]])[0][0]))
        
        st.write("AI's Predicted Profits (Regression): " + f'`{output1}`')
        st.write('----')
