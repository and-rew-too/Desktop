import plotly.graph_objects as go
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots

import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls
username = 'andrew.hu'
api_key = 'iVl6cjSPrLfIYfp75OTP'
tls.set_credentials_file(username=username, api_key=api_key)

pd.set_option('display.width', None)
df = pd.read_csv(
    "C:/Users/Andrew Hu/Dropbox/PC/Downloads/6-10-uniformity.csv")
workdf = pd.DataFrame()

coords = df["Sample_ID"].str.split("-", n = 6, expand = True)
workdf["ID"] = df["Sample_ID"]
workdf["Irr"] = df["Imp_(A)"]
workdf["xpos"] = coords[5]
workdf["ypos"] = coords[6]
print(workdf)
# workdf.iloc[23,1] = 4.20
# workdf.iloc[24,1] = 4.30

irrmean = workdf["Irr"].mean()
print(irrmean)
#Pmp standard deviation
P1 = (workdf.iloc[:,1].sub(irrmean)).pow(2)
P2 = P1.sum()
irrStandDev = (P2 / len(df.index))**(1/2)
print(irrStandDev)

#workdf.iloc[:,1] = workdf.iloc[:,1].div(irrmean) use this to plot a normalized irradiance

z = np.eye(6,10)
print(z)
for i in range(0,len(workdf.index)):
    X = int(workdf.iloc[i,2])
#    X = int(workdf.iloc[5-i,2]) use this to reverse orientation of x values, make ot go top to bottom
    Y = int(workdf.iloc[i,3])
    X = X-1
    Y = Y-1
    z[X][Y] = workdf.iloc[i,1]
print(z)

z1 = z*0
z1 = z1+irrmean


# fig = go.Figure(go.Surface(
#     contours = {
#         "y": {"show": True, "start": 4.0, "end": 6.0, "size": 0.04, "color":"white"},
#         "z": {"show": True, "start": 0.5, "end": 1.0, "size": 0.05}
#     },
#     x = [1,2,3,4,5],
#     y = [1,2,3,4,5,6,7,8,9,10],
#     z = z
#     ),
# )

fig = go.Figure(data=[
    go.Surface(z=z),
    go.Surface(z=z1, showscale=False, opacity=0.5)
])


fig.update_layout(
        scene = {
            "xaxis": {"nticks": 20},
            "zaxis": {"nticks": 8},
            "yaxis": {"nticks": 18},
            "aspectratio": {"x": 2, "y": 1, "z": 1},
            "xaxis":{"title":"x-cell position"},
             "yaxis":{"title":"y-cell position"},
             "zaxis":{"title":"I_mp(A)"}})

fig.show()






