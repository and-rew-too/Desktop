from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#for measurements of Voc, pFF, FF, based on different SAS cell etch depths and times
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=2106494240"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
workdf = df.iloc[:, [3, 4,5,6,7,8,9,10,11,12,13,14,39,40]]
print(workdf)
COL = 13 #incredibly important parameter must change this
# 123 is isc voc, 7 is ff, 12 is pff
Param = list(workdf.columns)[COL]
print(Param)

#x1 is SAS type C
#x3 is SAS type H
#x3 s huasun drilled mwt
x1 = workdf.iloc[0:5,COL]
x2 = workdf.iloc[5:10,COL]
x3 = workdf.iloc[10:58,COL]
fig = plt.figure(figsize=(9,6))


plt.boxplot([x for x in [x1, x2, x3]], 0, 'rs', 1)

plt.xticks([y+1 for y in range(len([x1, x2, x3]))], ['CA-183', 'PEDOT:PSS..', 'PEDOT & ,....'])
plt.xlabel('CONDUCTIVE ADHESIVE Group')
plt.ylabel(Param)
t = plt.title('Box plot of ' + Param)
plt.grid()
plt.show()