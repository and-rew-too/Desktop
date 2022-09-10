from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd

sheet_url = "https://docs.google.com/spreadsheets/d/1MJoo_LZrhD4qlF2OCJEpl-r85inmDwYIydU-xvpqWhc/edit#gid=1354516786"


url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)


fig = go.Figure()
#fig.add_trace(go.Scatter(x=df.iloc[:, 1], y=df.iloc[:, 2],
#                         mode='markers',
#                         name='markers'))
fig.add_trace(go.Scatter(x=df.iloc[0:3, 1], y=df.iloc[0:3, 2],
                         mode='lines+markers',
                         name='Tamb 46 modeled'))

# fig.add_shape(type="rect",
#     x0=100, x1=1100,
#     y0=72, y1=100,
#     fillcolor="LightSalmon", opacity=0.3,
#     layer="below", line_width=0,
# )

fig.update_layout(
    xaxis_title="Incoming Radiation [W/m2]",
    yaxis_title="T_t Temperature [C]",
    title="Module Temperature vs Irradiance (wind speed = 0 m/s)")
fig.update_layout(
    autosize=False,
    width=600,
    height=600,)
fig.update_layout(xaxis_range=[100, 1100])
fig.update_layout(yaxis_range=[50, 100])

fig.show()
