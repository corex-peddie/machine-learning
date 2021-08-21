import streamlit as st
from multiapp import MultiApp
from apps import finance, web, about

# import your app modules here

app = MultiApp()

st.set_page_config(page_title="CoreX Analysis App", page_icon="💲", layout='centered', initial_sidebar_state="collapsed")

st.markdown("""
# CoreX Analysis App
This app allows users to get recommendations and obtain useful metrics for their E-Commerce business through Machine Learning and AI
""")

# Add all your application here
app.add_app("Financial Analysis", finance.app)
app.add_app("SEO Analysis", web.app)
app.add_app('About', about.app)
# The main app
app.run()