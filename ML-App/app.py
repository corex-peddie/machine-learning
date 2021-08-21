import streamlit as st
from multiapp import MultiApp
from apps import home, finance, web

# import your app modules here

app = MultiApp()

st.markdown("""
# Corex Machine Learning App
This prototype app allows users to get recommendations and useful metrics regarding the performence and future of their E-Commerce business
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Financial Ratings", finance.app)
app.add_app("Website Analysis", web.app)
# The main app
app.run()