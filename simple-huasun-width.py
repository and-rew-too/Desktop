import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

sheet_url = "https://docs.google.com/spreadsheets/d/12RYFtjew1XxsE4Tf3L7E2ABPJv7y6wk80gXFf52WVzU/edit#gid=0"
pd.set_option('display.width', None)

url_1 = sheet_url.replace('/edit#gid=' , '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)


def objective(x, a, c):
	return a*(x**-1.286) + c
    # b was actually the x^n power had to enter manually to find a solution
    # find it here, in desmos link https://www.desmos.com/calculator/og5tjbyujk

x = df.iloc[:,1]
y = df.iloc[:,10]
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, c = popt
# interploting values from 15 mm to 160mm and plotting the new curve
x_new = np.linspace(15, 160, 146)
y_new = objective(x_new, a, c)


Jsc = 0.038
Rs = 1.05
Voc = 0.730
Vmp = Voc* (y_new/100 *(1-(Rs*Jsc/Voc) ) / 0.95 )
Imp = (Jsc * 16.6 * ((x_new*0.1)-0.5) ) * 0.95
Pmp = Imp*Vmp

#below, is ignoring other factors and looking at resistive losses from increasing length
ff_finger_laser = Voc* (y_new/100*(1-(Rs*Jsc/Voc) )) * (1-((0.00064*Jsc*(x_new/10)**2)/(48*0.0014*Voc)) )
resistloss = 0.83 * (1-((0.00064*Jsc*(x_new/10)**2)/(48*0.0014*Voc)) )
print(resistloss)
new_Pmp = ff_finger_laser*Imp


fig = make_subplots(
    rows=2, cols=3,
    subplot_titles=("pFF points", "fitted pFF","Voltage change/laser", "max Power","Final","Voltage change/fingers"))

fig.add_trace(go.Scatter(x=x, y=y),
              row=1, col=1)

fig.add_trace(go.Scatter(x=x_new, y=y_new),
              row=1, col=2)

fig.add_trace(go.Scatter(x=x_new, y=Vmp),
              row=1, col=3)
fig.add_trace(go.Scatter(x=x_new, y=Pmp),
              row=2, col=1)
fig.add_trace(go.Scatter(x=x_new, y=ff_finger_laser),
              row=2, col=2)
fig.add_trace(go.Scatter(x=x_new, y=new_Pmp),
              row=2, col=1)
fig.add_trace(go.Scatter(x=x_new, y=resistloss),
              row=2, col=3)

fig.update_layout(height=500, width=700,
                  title_text="Multiple Subplots with Titles")

fig.show()
