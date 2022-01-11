import plotly
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math

sheet_url = "https://docs.google.com/spreadsheets/d/1DlP7xF7aEk0xDsFkoAHK4fokn7nnX0AkwAXq0nBJSIs/edit#gid=0"


url_1 = sheet_url.replace('/edit#gid=' , '/export?format=csv&gid=')
val = pd.read_csv(url_1,)
print(val)

#LENGTH OF TRANSMISSION DATA IS 429
#len(df.index) = 429

df = pd.DataFrame(np.zeros([429,7]))
df.iloc[0,0] = 3
df.iloc[1,0] = 4
df.iloc[2,0] = 5

print(val.iloc[:,5])
for i in range(0,1000):
    if math.isnan(val.iloc[i,5])==True:
        print(i)
    else:
        print('nah')


# # base code to duplicate a row (n) this case (5) times into a new row
# set10 = 0
# newdf = pd.DataFrame(np.zeros([3*5,7]))
# for i in range(0,len(df.index)):
#     for j in range(set10,set10+5):
#         newdf.iloc[j,0] = df.iloc[i,0]
#     set10 = set10+5
# print(newdf)
