from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#for measurements of Voc, pFF, FF, based on different SAS cell etch depths and times
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=700330920"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
workdf = df.iloc[:, [3, 4,5,6,7,8,9,10,11,12,13,14,39,40]]
print(workdf)
COL = 7 #incredibly important parameter must change this
# 123 is isc voc, 7 is ff, 12 is pff
Param = list(workdf.columns)[COL]
print(Param)


#x1 is SAS type C
x1 = workdf.iloc[6:8,COL] #0:2
print(x1)
x2 = workdf.iloc[9:11,COL] #3:5
fig = plt.figure(figsize=(9,6))


plt.boxplot([x for x in [x1, x2]], 0, 'rs', 1)

plt.xticks([y+1 for y in range(len([x1, x2]))], ['ECA', 'PEDOT (PH1000)-DMSO'])
plt.xlabel('Conductive Adhesive Type')
plt.ylabel('FF [%]')
t = plt.title('Box plot of Fill Factor 3Hours 85C')
plt.ylim([60,80])
plt.grid()
plt.show()