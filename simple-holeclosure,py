import plotly
import plotly.graph_objects as go
import numpy as np
import pandas as pd

sheet_url = "https://docs.google.com/spreadsheets/d/1NQ2vTYFpf6MrydWY328F85zL1Y0ZBTqKMFuTUcEzQ6w/edit#gid=0"


url_1 = sheet_url.replace('/edit#gid=' , '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)





fig = go.Figure()
fig.add_trace(go.Scatter(x=df.iloc[:,1], y=df.iloc[:,2],
                    mode='markers',
                    name='markers'))
fig.add_trace(go.Scatter(x=df.iloc[:,1], y=df.iloc[:,5],
                    mode='markers',
                    name='markers'))

fig.add_shape(type="rect",
    x0=1, x1=2.5, y0=0, y1=5.0, fillcolor="LightSalmon", opacity=0.3, line_color="LightSalmon")
fig.add_shape(type='line',
                x0=1,
                y0=0.8,
                x1=4,
                y1=0.8,
                line={'dash': 'dash', 'color': 'red'},
                xref='x',
                yref='y'
)
fig.add_shape(type='line',
                x0=1,
                y0=1.5,
                x1=4,
                y1=1.5,
                line={'dash': 'dash', 'color': 'red'},
                xref='x',
                yref='y'
)
fig.update_layout(
    xaxis_title="Cut Diameter [mm]",
    yaxis_title="Final diameter [mm]",
    title="Scatterplot of Hole Closure 11-18 [100 micron 150C]")

fig.show()
