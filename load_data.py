'''
Walker Frankenberg & Daniel Brey
10/14/21
This script loads the data (which we received in html format) and creates pandas dataframes from them, exporting them to csv files.
'''

# Import packages
import pandas as pd
import os
import datetime

# Get the directory and the subfolders in the directory
cur_dir = os.getcwd()
data_dir = cur_dir + "/data"
folders = next(os.walk(data_dir))[1]

# Look at the data for each year
for curr_year_folder in folders:
  curr_year_dir = data_dir + "/" + curr_year_folder
  year_df_list = []
  # Look at each file in the directory, where each file corresponds to a month's worth of data
  for file_name_ext in next(os.walk(curr_year_dir))[2]:
    if (file_name_ext[-4:] != '.xls'):
      continue
    index = 0
    file_name = file_name_ext[0:-4]
    curr_path = curr_year_dir + "/" + file_name_ext
    
    #print(curr_path)
    df = pd.read_html(curr_path)
    date = df[index].columns.tolist()
    
    month_df_list = []
    # Loops through each day in the month and make edits, as the html code is super ugly
    while (index < len(df) - 2): # Ignore the last two, the month summary and an empty dataframe
      date_time = []
      
      date = df[index].columns.tolist()
      
      # If for the day, there is "No demand data found", we want to skip them
      if date[0][0:3] == "No ": 
        index += 1
      
      # Otherwise, create a dataframe for that day
      else:
        date = datetime.datetime.strptime(date[0][14:26], '%b %d, %Y')
        times = df[index+1][('Time', 'Time')].tolist()
        avg_demand = df[index+1][('Total Avg. Demand (kW)', 'Total Avg. Demand (kW)')].tolist()
        peak = df[index+1][('By Data Series', 'Campus Electrical / Main Campus Peak Meter (kW)')].tolist()
        off_peak = df[index+1][('By Data Series', 'Campus Electrical / Main Campus Off Peak Meter (kW)')].tolist()
        
        for count, element in enumerate(times):
          element = datetime.datetime.strptime(element, '%H:%M').time()
          element = datetime.datetime.combine(date, element)
          
          times[count] = element
        
        # Create a pandas dataframe for each day's data, and append it to a list for the whole month
        packed_data = {'Time': times, 'Average Demand': avg_demand, 'Peak' : peak, 'Off Peak' : off_peak}
        day_dataframe = pd.DataFrame(data = packed_data)
        month_df_list.append(day_dataframe)
        
        index += 2

    # If there is data for that month, create a dataframe out of each day of that month's data and append it to the list for the year
    if (month_df_list != []):
      month_dataframe = pd.concat(month_df_list)
      year_df_list.append(month_dataframe)

  # Create a dataframe for the year from each month's data
  year_dataframe = pd.concat(year_df_list)
  year_dataframe = year_dataframe.sort_index()

  # Save the dataframe to a csv file
  file_name = curr_year_dir + '/' + curr_year_folder + '.csv'
  year_dataframe.to_csv(path_or_buf=file_name)
  print(year_dataframe)
