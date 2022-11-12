import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls


from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd

#username = 'andrew.hu'
#api_key = 'iVl6cjSPrLfIYfp75OTP'
#tls.set_credentials_file(username=username, api_key=api_key)



pd.set_option('display.width', None)
df = pd.read_csv(
    "C:/Users/andre/Downloads/KAUST-data.csv")
#df = df.sort_values(by = 'Measurement_Date-Time', ascending = False)

print(df)


Hdf = df[df.iloc[:,1].str.contains("HAST")]


fig = make_subplots(rows=1, cols=5, subplot_titles=("against Pmax",
                                                    "against dIsc",
                                                    "against dFF",
                                                    "against dVoc",
                                                    "against dpFF",
                                                    ))
fig.append_trace(go.Scatter(
        x=Hdf.iloc[:, 2], y=Hdf['dPmax'], text=Hdf.iloc[:, 0], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=1, col=1)

fig.append_trace(go.Scatter(
        x=Hdf.iloc[:, 2], y=Hdf['dIsc'], text=Hdf.iloc[:, 0], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=1, col=2)
fig.append_trace(go.Scatter(
        x=Hdf.iloc[:, 2], y=Hdf['dFF'], text=Hdf.iloc[:, 0], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=1, col=3)
fig.append_trace(go.Scatter(
        x=Hdf.iloc[:, 2], y=Hdf['dVoc'], text=Hdf.iloc[:, 0], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=1, col=4)
fig.append_trace(go.Scatter(
        x=Hdf.iloc[:, 2], y=Hdf['dPFF'], text=Hdf.iloc[:, 0], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=1, col=5)


fig.add_shape(type='line',
                x0=0,
                y0=-5,
                x1=100,
                y1=-5,
                line={'dash': 'dash', 'color': 'black'},
                xref='x',
                yref='y'
)
fig.add_shape(type='line',
                x0=0,
                y0=0,
                x1=100,
                y1=0,
                line={'dash': 'dash', 'color': 'black'},
                xref='x',
                yref='y'
)
fig.add_shape(type='line',
                x0=0,
                y0=5,
                x1=100,
                y1=5,
                line={'dash': 'dash', 'color': 'black'},
                xref='x',
                yref='y'
)

fig.update_layout(font=dict(
        family="Georgia",
        size=18,
        color="RebeccaPurple"
    )
)
fig.update_yaxes(range=[-40, 0], dtick=5)
fig.show()
