import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import average_demand,day_average_demand # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Green Midd")

# Add all your applications (pages) here
app.add_page("Average Demand", average_demand.app)
app.add_page("30 Day Average Demand", day_average_demand.app)

app.run()
