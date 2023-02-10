import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#for measurements of Voc, pFF, FF, based on different SAS cell etch depths and times
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=1794705851"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
print(df)
workdf = df
#workdf = df.iloc[:, [0, 1,2,3,4,5,6,7]]
#print(workdf)

#1 is ctrl
#5 is dh
# 9 10 11 is h
COL = 1 #incredibly important parameter must change this #1, 9 ,10
#START3 FOR NEXT ROW is 0,9, 18, 27, 36
start3 = 18

if start3 == 0:
    Param = "Tedlar "
elif start3 == 9:
    Param = "Maxeon Front "
elif start3 == 18:
    Param = "Maxeon Rear "
elif start3 == 27:
    Param = "DSC "
elif start3 == 36:
    Param = "ECTFE "
elif start3 == 45:
    Param = "FEP "
else:
    Param = "nah"
column_headers = df.columns.values.tolist()
Param = Param+column_headers[COL]

#Param = "Maxeon Rear - HF5"

x1 = workdf.iloc[start3:start3+3,COL]
x2 = workdf.iloc[start3+3:start3+6,COL]
x3 = workdf.iloc[start3+6:start3+9,COL]

x12 = workdf.iloc[start3:start3+3,7]
x22 = workdf.iloc[start3+3:start3+6,7]
x32 = workdf.iloc[start3+6:start3+9,7]
x13 = workdf.iloc[start3:start3+3,8]
x23 = workdf.iloc[start3+3:start3+6,8]
x33 = workdf.iloc[start3+6:start3+9,8]
# x14 = workdf.iloc[start3:start3+3,11]
# x24 = workdf.iloc[start3+3:start3+6,11]
# x34 = workdf.iloc[start3+6:start3+9,11]
print(workdf.iloc[start3+3:start3+6,COL])


fig = plt.figure(figsize=(12,9))
plt.boxplot([x for x in [x1,x12,x13,x14, x2,x22,x23,x24,x3,x32,x33,x34]], 0, 'rs', 1)
plt.xticks([y+1 for y in range(len([x1,x12,x13,x14, x2,x22,x23,x24,x3,x32,x33,x34]))],
           ['Ctrl baseline','TS100 baseline', 'TS200 baseline','Ctrl 2mil','TS100 2mil', 'TS200 2mil', 'Ctrl 1mil','TS100 1mil', 'TS200 1mil'])
plt.ylabel('Peel Strength [N/mm]')

Param = 'Maxeon Rear Interface, Thermal Shock Testing'
t = plt.title('Box plot of ' + Param)
plt.xticks(rotation=20)
plt.ylim([0,7.5]) # 0 to 5.5 # 0 to 2.5
plt.grid()
plt.show()