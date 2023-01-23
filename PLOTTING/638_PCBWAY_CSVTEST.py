import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


dfL130 = pd.read_csv("C:/Users/andre/Downloads/PCBWAYTEST.txt", skiprows=1, sep='\t', engine='python')
print(dfL130.iloc[12,:])


x = dfL130.iloc[2,:])
y = dfL130.iloc[3,:])
val = dfL130.iloc[4,:])
x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))
fig.show()