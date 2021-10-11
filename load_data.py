import pandas as pd
import os
import glob

from lxml import etree

col_names = ["Time", "Total Average Demand (kW)", "Campus Electrical / Main Campus Peak Meter (kW)", "Campus Electrical / Main Campus Off Peak Meter"]

cur_dir = os.getcwd()
data_dir = cur_dir + "/data"


folders = next(os.walk(data_dir))[1]


for curr_year_folder in folders:
  print(curr_year_folder)
  curr_year_dir = data_dir + "/" + curr_year_folder
  df_list = []
  
  for file_name_ext in next(os.walk(curr_year_dir))[2]:
    index = 0
    file_name = file_name_ext[0:-4]
    #print(file_name)
    curr_path = curr_year_dir + "/" + file_name_ext
    df = pd.read_html(curr_path)
    date = df[index].columns.tolist()
    
    print(len(df))
    
    while (index < len(df) - 2): # Ignore the last two, the month summary and an empty dataframe
      date = df[index].columns.tolist()
      if date[0][0:2] == "No ": # No demand data found, we want to skip these
        print("None")
        index += 1
        
      else:
        date = date[0][14:26]
        print(date)
      
        print(df[index + 1].columns.tolist())
        # Take the time and merge with date
        # Take the other column values and put them in the dataframe
        print(df[index+1].iloc[:,0:3])

        df_list.append(df)
        
        index += 2

  
    
  #for dataframe in df_list:
    #print(dataframe.index.tolist())
  #df1 = pd.concat(df_list)  ## concatenating all the individual files 
  #df1.to_csv('{}/{}_full_year.csv'.format(data_dir, curr_year_folder[-4:]))
    
  break