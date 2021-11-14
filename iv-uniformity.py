import plotly.graph_objects as go
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots

pd.set_option('display.width', None)
df = pd.read_csv(
    "C:/Users/Andrew Hu/Dropbox/PC/Downloads/6-10-uniformity.csv")
workdf = pd.DataFrame()

coords = df["Sample_ID"].str.split("-", n = 4, expand = True)
workdf["ID"] = df["Sample_ID"]
workdf["Irr"] = df["Imp_(A)"]
workdf["xpos"] = coords[3]
workdf["ypos"] = coords[4]
print(workdf)
workdf.iloc[23,1] = 4.20
workdf.iloc[24,1] = 4.30

irrmean = workdf["Irr"].mean()
print(irrmean)
#Pmp standard deviation
P1 = (workdf.iloc[:,1].sub(irrmean)).pow(2)
P2 = P1.sum()
irrStandDev = (P2 / len(df.index))**(1/2)
print(irrStandDev)

z = np.eye(10,5)
print(z)
for i in range(0,len(workdf.index)):
    X = int(workdf.iloc[i,2])
    Y = int(workdf.iloc[i,3])
    X = X-1
    Y = Y-1
    z[X][Y] = workdf.iloc[i,1]
print(z)

fig = go.Figure(go.Surface(
    contours = {
        "y": {"show": True, "start": 4.0, "end": 6.0, "size": 0.04, "color":"white"},
        "z": {"show": True, "start": 0.5, "end": 1.0, "size": 0.05}
    },
    x = [1,2,3,4,5],
    y = [1,2,3,4,5,6,7,8,9,10],
    z = z,
    ))

fig.update_layout(
        scene = {
            "xaxis": {"nticks": 8},
            "zaxis": {"nticks": 20},
            "yaxis": {"nticks": 18},
            "aspectratio": {"x": 1, "y": 2, "z": 1}})

fig.show()








