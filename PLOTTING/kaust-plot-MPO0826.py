from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#for measurements of Voc, pFF, FF, based on different SAS cell etch depths and times
sheet_url = "https://docs.google.com/spreadsheets/d/1MJoo_LZrhD4qlF2OCJEpl-r85inmDwYIydU-xvpqWhc/edit#gid=2030468464"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
print(df)

workdf = df.iloc[:, [3, 4,5,6,7,8,9,10,11,12,13,14,39,40]]
print(workdf)


COL = 9 #incredibly important parameter must change this
Param = list(workdf.columns)[COL]
print(Param)

x1 = workdf.iloc[0:4,COL]
x2 = workdf.iloc[12:16,COL]
x3 = workdf.iloc[18:22,COL]
x4 = workdf.iloc[24:28,COL]
x5 = workdf.iloc[30:34,COL]
x6 = workdf.iloc[36:40,COL]
x7 = workdf.iloc[42:46,COL]
x8 = workdf.iloc[48:52,COL]
x9 = workdf.iloc[54:58,COL]
x10 = workdf.iloc[60:64,COL]
x11 = workdf.iloc[66:70,COL]

fig = plt.figure(figsize=(12,9))


plt.boxplot([x for x in [x1, x2, x3, x4, x5,x6,x7,x8,x9,x10,x11]], 0, 'rs', 1)

plt.xticks([y+1 for y in range(len([x1, x2, x3,x4, x5,x6,x7,x8,x9,x10,x11]))], ['a', 'C', 'D','E','F','G','H','I','J','K','L'])
plt.xlabel('Parameters')
plt.ylabel(Param)
t = plt.title('Box plot of ' + Param)
plt.grid()
plt.show()
