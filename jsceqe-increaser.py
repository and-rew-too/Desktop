from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math

sheet_url = "https://docs.google.com/spreadsheets/d/1DlP7xF7aEk0xDsFkoAHK4fokn7nnX0AkwAXq0nBJSIs/edit#gid=52760202"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
val = pd.read_csv(url_1,)

df = pd.DataFrame(np.zeros([81, 7]))
#column 2, for etfe ctrl
newdf = pd.DataFrame(np.zeros([81*5, 9]))

set5 = 0
for i in range(0, len(val.index)):
    if math.isnan(val.iloc[i, 1]) == False:
        for j in range(set5, set5+5):
            newdf.iloc[j, 4] = val.iloc[i, 1]
        set5 = set5+5
        #end
    else:
        continue

print(newdf)
newdf.to_csv("C:/Users/andre/Desktop/sunpowertest.csv",encoding='utf-8')
