import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import os
import matplotlib.pyplot as plt

# 30 Day Average of Demand
def get_30_day_avg(dataframe, column = 'Average Demand'):
  window_size = 30
  window_inc = 1
  
  smoothed_impulse = []

  value_list = dataframe[column]
  nwindows = len(value_list)

  for wind in range(nwindows):
      begin_ind = int(wind*window_inc-window_size/2)
      end_ind = int(wind*window_inc+window_size/2)
      window_avg = np.nanmean(value_list[begin_ind:end_ind])
      smoothed_impulse.append(window_avg)
  smoothed_impulse = np.asarray(smoothed_impulse)
  return smoothed_impulse

# Load the dataframe from the csv files
def get_energy_dataframe():
  # Get the directory and the subfolders in the directory
  cur_dir = os.getcwd()
  data_dir = cur_dir + "/data"
  folders = next(os.walk(data_dir))[1]
  df_list = []
  for curr_year_folder in folders:
    file_name = data_dir + '/' + curr_year_folder + '/' + curr_year_folder + '.csv'
    df = pd.read_csv(file_name)
    df_list.append(df)

  total_energy = pd.concat(df_list)
  return total_energy

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
fig1.patch.set_facecolor('#EBEBEB')

ax1.pie(sizes,
        )
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.



def app():
  total_energy = get_energy_dataframe()
  

  datetimes_as_strings = total_energy["Time"]
  #print(type(datetimes_as_strings))
  datetimes_replace = datetimes_as_strings.str.replace(' ', '-')
  datetimes_split = datetimes_replace.str.split('-')
  datetimes_day = datetimes_split.apply(pd.Series)[2]
  datetimes_month = datetimes_split.apply(pd.Series)[1]
  datetimes_year = datetimes_split.apply(pd.Series)[0]

  total_energy["Date"] = datetimes_year + '-' + datetimes_month + '-' + datetimes_day 
  #print(len(total_energy['Date'].unique().tolist())) 
  days_filter = datetimes_day.astype('int')%15 == 0
  total_energy = total_energy[days_filter]
  
  total_energy = total_energy.groupby('Date', group_keys=False).apply(lambda df: df.sample(1))




  day_avg = get_30_day_avg(total_energy)

  total_energy['30 Day Average Demand'] = day_avg

  #First line graph option - uses altair
  
  _, col2 = st.columns([.1, 4])

  with col2:
    st.header('Average Energy Demand')
  chart_line = alt.Chart(total_energy).mark_line().encode(
    alt.X('Date:T', timeUnit = 'yearmonthdate'),
    y='Average Demand'
  )
  st.altair_chart(chart_line, use_container_width=True)

  metric1, metric2, metric3 = st.columns([5,5,5])

  with metric1:
    st.metric('Usage: Past 24 Hours', 42, 2)
  with metric2:
    st.metric('Usage: Past Week', 42, 2)
  with metric3:
    st.metric('Usage: Past Month', 42, 2)

  st.pyplot(fig1)