from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd


sheet_url = "https://docs.google.com/spreadsheets/d/1MJoo_LZrhD4qlF2OCJEpl-r85inmDwYIydU-xvpqWhc/edit#gid=635872875"


url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)


fig = go.Figure()
#fig.add_trace(go.Scatter(x=df.iloc[:, 1], y=df.iloc[:, 2],
#                         mode='markers',
#                         name='markers'))
fig.add_trace(go.Scatter(x=df.iloc[0:5, 1], y=df.iloc[0:5, 3],
                         mode='lines+markers',
                         name='Tamb 10 modeled'))
fig.add_trace(go.Scatter(x=df.iloc[5:10, 1], y=df.iloc[5:10, 3],
                         mode='lines+markers',
                         name='Tamb 20 modeled'))
fig.add_trace(go.Scatter(x=df.iloc[10:15, 1], y=df.iloc[10:15, 3],
                         mode='lines+markers',
                         name='Tamb 30 modeled'))
fig.add_trace(go.Scatter(x=df.iloc[15:20, 1], y=df.iloc[15:20, 3],
                         mode='lines+markers',
                         name='Tamb 40 modeled'))
#BELOW IS THE ACTUAL PHYSICAL MEASUREMENTS
#fig.add_trace(go.Scatter(x=[710], y=[59.18],
#                         mode='markers',
#                         marker=dict(size=12, color="Black"), name='30C Lower Irradiance Measured'))
#fig.add_trace(go.Scatter(x=[1000], y=[64.25],
#                         mode='markers',
#                         marker=dict(size=12, color="Black"), name='30C Higher Irradiance Measured'))


fig.update_layout(
    xaxis_title="Incoming Radiation [W/m2]",
    yaxis_title="T_b1 Temperature [C]",
    title="Module Temperature vs Irradiance (wind speed = 0 m/s)")
fig.update_layout(
    autosize=False,
    width=800,
    height=800,)
fig.update_layout(xaxis_range=[100, 1100])
#fig.update_layout(yaxis_range=[0, 80])

fig.show()
