import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np



xs = ["SUV 24", "SUV 100", "SUV100+HAST12","SUV100+HAST24"]
xh = ["HAST 30", "HAST 100", "SUV100+HAST30","SUV100+HAST60"]
#y = [1,1,1,1,2,10,10,12,8,10,13,13,13,13,13]
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("pFF points", "fitted pFF","Voltage change/laser", "max Power"))

# agc sequential suv hast
fig.add_trace(go.Scatter(
        x=xs,
        y=[0, 0, 0, 0],
        name='AGC doubleside',
        marker_color="black"
    ),row=1,col=1)
# etfe sequential suv hast
fig.add_trace(go.Scatter(
        x=xs,
        y=[33.9, 31.1, 31, 300],
        name='ETFE ctrl',
        marker_color="blue"
    ),row=1,col=2)
# agc sequential hast -suv
fig.add_trace(go.Scatter(
        x=xh,
        y=[43, 42, 32.1, 16.4],
        name='AGC doubleside',
        marker_color="grey"
    ),row=2,col=1)
# etfe sequential hast -suv
fig.add_trace(go.Scatter(
        x=xh,
        y=[38.62, 6.48, 0.88, 1.74],
        name='ETFE ctrl',
        marker_color="lightskyblue"
    ),row=2,col=2)
fig.update_yaxes(range=[0, 45], dtick=5.0)
fig.show()
