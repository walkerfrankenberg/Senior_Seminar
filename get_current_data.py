import requests
from datetime import datetime
import pandas as pd
import io

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
  print(df)