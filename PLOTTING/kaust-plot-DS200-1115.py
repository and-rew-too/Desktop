from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator

#for meausrements of Voc, pFF, FF based on different heating profiles of huasun hjt cells
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=453460291"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
print(df)


workdf = df.iloc[:, [3, 4,5,6,7,8,9,10,11,12,13,14,21,39,40]]
print(workdf)

import matplotlib.pyplot as plt


#2,3,4,5,6,7,8,10,12,13

COL = 14 #incredibly important parameter must change this
column_headers = workdf.columns.values.tolist()
param = column_headers[COL]

x0 = workdf.iloc[0,COL] # reference cell only use the best one
x1 = workdf.iloc[1,COL]
x2 = workdf.iloc[2,COL]



fig = plt.figure(figsize=(5,18))
#plt.boxplot([x for x in [x0, x1, x2]], 0, 'rs', 1)
c = ['blue', 'blue', 'blue', 'bisque']
plt.bar(workdf.iloc[:,0], workdf.iloc[:,COL], color = c)
ylimdf = workdf.iloc[:,COL]
maximum = ylimdf.max()
Ymax = maximum + maximum*0.12
Ymin = maximum - maximum*0.22 #change to 2 for Rs

ml = MultipleLocator(8)
plt.ylim([Ymin, Ymax])
plt.xticks(rotation=20)
#plt.xlabel('Cell Type')
plt.ylabel('{}'.format(param))
t = plt.title('Box plot of {}'.format(param))
plt.show()
