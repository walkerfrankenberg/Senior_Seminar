import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import test_page,test_page_2 # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Data Storyteller Application")

# Add all your applications (pages) here
app.add_page("30 Day Average Demand", test_page.app)
app.add_page("Average Demand", test_page_2.app)

# The main app
app.run()