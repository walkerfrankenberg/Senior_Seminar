import streamlit as st
import pandas as pd
import altair as alt

from shared import get_energy_dataframe, pie_chart
from get_current_data import get_metrics_data, load_day_data


def app():
  total_energy = get_energy_dataframe()
  real_time_energy = load_day_data(3, 11, 2021)
  real_time_energy.columns = ["Time", "location", "Average Demand"]

  
  datetimes_as_strings = real_time_energy.iloc[:,0]
  datetimes_split = datetimes_as_strings.str.split('T')

  _, col2 = st.columns([.1, 4])

  with col2:
    st.header('Real Time - Average Energy Demand')
  chart_line = alt.Chart(real_time_energy).mark_line().encode(
    alt.X('Time:T', timeUnit = 'hoursminutesseconds'),
    y='Average Demand'
  )
  st.altair_chart(chart_line, use_container_width=True)

  metric1, metric2, metric3 = st.columns([8,8,8])

  with metric1:
    day, day_diff, week, week_diff = get_metrics_data()
    st.metric('Usage: Today', "{} kW".format(day), "{}%".format(day_diff))
  with metric2:
    st.metric('Usage: Past Week', "{} kW".format(week), "{}%".format(week_diff))
  with metric3:
    st.metric('Usage: Past Month', 42, 2)
