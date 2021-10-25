import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import os

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


def app():
  total_energy = get_energy_dataframe()

  day_avg = get_30_day_avg(total_energy)

  total_energy['30 Day Average Demand'] = day_avg

  #First line graph option - uses altair
  st.title('Energy2028 Data Visuals')
  chart_line = alt.Chart(total_energy).mark_line().encode(
    x='Time',
    y='Average Demand'
  ).properties(title="Sample Graph"
  )
  st.write("altair line chart below")
  st.altair_chart(chart_line, use_container_width=True)