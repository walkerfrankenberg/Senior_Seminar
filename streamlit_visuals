import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.title('Energy2028 Data Visuals')


sample = {'Time': [1, 2, 3, 4], 'Total Average Demand (kW)': [2, 3, 4, 3], 'Campus Electrical / Main Campus Peak Meter (kW)': [3, 3, 5, 5], 'Campus Electrical / Main Campus Off Peak Meter': [0, 0, 1, 2]}
sample_df = pd.DataFrame(data=sample)


#Tried randomizing - it should work
random_df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['Total Average Demand (kW)', 'Campus Electrical / Main Campus Peak Meter (kW)', 'Campus Electrical / Main Campus Off Peak Meter'])
time = [1,2,3,4,5,6,7,8,9,10]
random_df['Time'] = time

#Note: If the dataframe below doesn't work, sample_df can be used above.
df = sample_df.melt('Time', var_name='Measurement', value_name='Value') #Make the three measurements into kinda one column, so we can line chart them together


#First line graph option - uses altair
chart_line = alt.Chart(df).mark_line().encode(
  x='Time',
  y='Value',
  color= 'Measurement'
).properties(title="Sample Graph")
st.write("altair line chart below")
st.altair_chart(chart_line, use_container_width=True)

#Second line graph option - uses st.line_chart
df_index = df.rename(columns={'Time':'index'}).set_index('index')
st.write("st line chart below")
st.line_chart(df_index)
st.write("st area chart below")
st.area_chart(df_index)



chart_area = alt.Chart(df).mark_area().encode(
    x='Time',
    y='Value',
    color='Measurement',
    order='Measurement'
)
st.write("altair area chart below")
st.altair_chart(chart_line, use_container_width=True)



