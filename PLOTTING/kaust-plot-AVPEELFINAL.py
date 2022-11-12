import numpy as np
import pandas as pd
import pygsheets
import matplotlib.pyplot as plt

# Converts messy csv data from instron, into neat columns in google sheet for later plotting
# READ DOCUMENTATION BELOW
# https://pygsheets.readthedocs.io/en/latest/worksheet.html

col = 40
peelcsv = "C:/Users/andre/Downloads/AVPEEL/Specimen_RawData_" + str(col) + ".csv"

#opening spreadsheet to write csv into
gc = pygsheets.authorize(
    service_file='C:/Users/andre/Downloads/fluent-outlet-329800-d7ce5f1f4cd1.json')
sh = gc.open('AV-PARTTRACKER')
wks = sh.worksheet('title','Sheet10')

#opening csv data to parse data
df = pd.read_csv(peelcsv,skiprows=[0,1,2,3,4])
PEEL = df.iloc[:,2]

namedf = pd.read_csv(peelcsv,error_bad_lines=False)
title_list = namedf.iloc[1,1]
TITLE = pd.DataFrame([title_list], columns=['temp'])
#PEELLOAD = PEEL.append(TITLE, ignore_index = True)

BACK = PEEL.T.values.tolist() #convert list, BUT MUST BE TRANSPOSED
wks.update_col(col+1, BACK) #add one because sheets not pythonic, 1-indexed
wks.update_value((1,col+1), title_list) #updating the header row, with peel title



#reading values test, stored as list
B = wks.get_row(2, returnas='matrix')
print(B)
print(type(B))
