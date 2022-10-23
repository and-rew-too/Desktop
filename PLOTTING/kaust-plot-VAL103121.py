import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls


from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd


url_1 = 'C:/Users/andre/Downloads/huasun-modules - Sheet1.csv'
df = pd.read_csv(url_1,)
print(df)

Projstr = 'D2'

MindexNames = df[(df.iloc[:, 5] >= 2.0) | (df.iloc[:, 5] <= 1.0) | (
    df.iloc[:, 40] <= 0) | (df.iloc[:, 6] <= 0.4) ].index
df.drop(MindexNames, inplace=True)
#condition to only choose a specific Batch_ID \ Project ID
projectboolean = df[~df['Batch_ID'].str.contains(Projstr)]
df.drop(projectboolean.index, inplace=True)
# comments row, if left blank, is NaN, if filled is string df.iloc[:, 116]
df.iloc[:,3] = df.iloc[:,3].fillna('')
df.iloc[:,116] = df.iloc[:,116].fillna('')

pd.set_option('display.width', None)
final_DH = df





workdf = final_DH.iloc[:,[0,3,116,5,6,7,8,9,10,11,39]] #creates truncated df, very important we are using this now
print(workdf)


fig = make_subplots(rows=3, cols=2, subplot_titles=("Isc",
                                                    "pFF",
                                                    "FF",
                                                    "Efficiency",
                                                    "n/a",
                                                    "n/a"))

fig.append_trace(go.Scatter(
        x=workdf.iloc[:, 4], y=workdf['Isc_(A)'], text=workdf.iloc[:, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=1, col=1)

fig.append_trace(go.Scatter(
        x=workdf.iloc[:, 4], y=workdf['pFF_(percent)'], text=workdf.iloc[:, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=1, col=2)

fig.append_trace(go.Scatter(
        x=workdf.iloc[:, 4], y=workdf['FF_(percent)'], text=workdf.iloc[:, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=2, col=1)

fig.append_trace(go.Scatter(
        x=workdf.iloc[:, 4], y=workdf['Efficiency_(percent)'], text=workdf.iloc[:, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=2, col=2)
fig.update_layout(height=600, width=600,
                  title_text="Scatterplots of Voc versus Electrical Parameters")
fig.update_annotations(font_size=12)

#fig.update_yaxes(range=[-11, 2], dtick=1)
fig.show()
