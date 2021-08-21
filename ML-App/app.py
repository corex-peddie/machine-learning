import streamlit as st
from multiapp import MultiApp
from apps import home, finance, web

# import your app modules here

app = MultiApp()

st.set_page_config(page_title="CoreX ML App", page_icon="💲", layout='centered', initial_sidebar_state="collapsed")

st.markdown("""
# CoreX Machine Learning App
This app allows users to get recommendations and useful metrics regarding the performence and future of their E-Commerce business
""")

# Add all your application here
app.add_app("Website Analysis", web.app)
app.add_app("Financial Ratings", finance.app)
app.add_app("About", home.app)
# The main app
app.run()