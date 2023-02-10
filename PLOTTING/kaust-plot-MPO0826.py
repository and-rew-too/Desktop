from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#for measurements of Voc, pFF, FF, based on different SAS cell etch depths and times
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=1794705851"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
print(df)

workdf = df.iloc[:, [0, 1,2,6,7,8]]
print(workdf)


COL = 1 #incredibly important parameter must change this
Param = list(workdf.columns)[COL]
print(Param)

x1 = workdf.iloc[1:4,COL]
x2 = workdf.iloc[4:6,COL]


fig = plt.figure(figsize=(12,9))


plt.boxplot([x for x in [x1, x2,]], 0, 'rs', 1)

plt.xticks([y+1 for y in range(len([x1, x2]))], ['a', 'C'])
plt.xlabel('Parameters')
plt.ylabel(Param)
t = plt.title('Box plot of ' + Param)
plt.grid()
plt.show()
