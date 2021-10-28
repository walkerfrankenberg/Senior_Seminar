from numpy import datetime_as_string
import requests
from datetime import datetime
import pandas as pd
import io
import re
curr_time = datetime.now()

curr_min = curr_time.minute
curr_year = curr_time.year
curr_month = curr_time.month
curr_day = curr_time.day

url = "https://observatory.middlebury.edu/campus/energy/archive/"
curr_min = 1
if (curr_min % 60 == 1):
  url +=  "{}{}{}-campus.csv".format(curr_year, curr_month, curr_day)
  print(url)
  data = requests.get(url).content
  print("Got Data")
  df = pd.read_csv(io.StringIO(data.decode('utf-8')))

  datetimes_as_strings = df.iloc[:,0]
  datetimes_replace = datetimes_as_strings.str.replace(':', '-')
  datetimes_split = datetimes_replace.str.split('-')
  datetimes_minute = datetimes_split.apply(pd.Series)[3]
  minutes_filter = datetimes_minute.astype('int')%10 == 0

  df[minutes_filter]


  print(df[minutes_filter])