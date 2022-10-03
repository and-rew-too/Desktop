import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls


from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# FOR 3-5 REL MODULES gid=1055303193

sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=262898931"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)

###########like a museum Please Look but Do Not Touch ##############
#pd.set_option('display.width', None)
#df = pd.read_csv(
#    "C:/Users/Andrew Hu/Dropbox/PC/Downloads/All-Val-Modules.csv")
#df = df.sort_values(by='Measurement_Date-Time', ascending=True)

MindexNames = df[(df.iloc[:, 6] <= -0.1) | (
    df.iloc[:, 40] <= 0)].index
df.drop(MindexNames, inplace=True)
#condition to only choose a specific Batch_ID \ Project ID
#projectboolean = df[~df['Batch_ID'].str.contains(Projstr)]
#df.drop(projectboolean.index, inplace=True)
# comments row, if left blank, is NaN, if filled is string df.iloc[:, 116]
df.iloc[:, 3] = df.iloc[:, 3].fillna('')
df.iloc[:, 116] = df.iloc[:, 116].fillna('')


for i in range(0, len(df.index)):
    b = df.iloc[i, 5]*100
    if b//1000 >= 1:
        c = 4
    elif b//100 >= 1:
        c = 3
    elif b//10 >= 1:
        c = 2
    else:
        c = 1
    df.iloc[i, 5] = df.iloc[i, 5].round(decimals=c)
for j in range(6, 9):
   df.iloc[:, j] = df.iloc[:, j].round(decimals=4)
for k in range(9, 12):
   df.iloc[:, k] = df.iloc[:, k].round(decimals=4)
for m in range(38, 41):
   df.iloc[:, m] = df.iloc[:, m].round(decimals=4)
pd.set_option('display.width', None)

HASTboolean = df[df.iloc[:, 116].str.contains("HAST-25")]
print(HASTboolean)


int_DH = []
for n in range(0, len(HASTboolean.index)):
    str = HASTboolean.iloc[n, 3]
    str = str[3:]
    #print(str)
    for o in range(0, len(df.index)):
        samples = df.iloc[o, 3]
        #print(Samples)
        if samples.find(str) != -1:
            int_DH.append(df.iloc[o, :])
        else:
            pass
final_DH = pd.concat(int_DH, axis=1)
final_DH = final_DH.transpose()
print(final_DH)


# creates truncated df, very important we are using this now
workdf = final_DH.iloc[:, [0, 3, 116, 5, 6, 7, 8, 9, 10, 11, 39]]
print(workdf)
#comment this shit out of this one bro.. head scratcher forreal
#so first creates a new column that will be filled
#looping through the length , started at second row
#it checks the top row, row above, to see if it was iv data created at a later or earlier date
#if the iv data was created at a earlier date e.g. (df.i-1,0 < df.i,0)
# that means that the data above is for the same part
# so if true, then index the new column as the same part id
#and if not true, then create a new index number, as a new part id
workdf.loc[:, 'partid,loop'] = 0
for i in range(1, len(workdf.index)):
    if workdf.iloc[i-1, 0].astype(int) < workdf.iloc[i, 0].astype(int):
        workdf.iloc[i, 11] = workdf.iloc[i-1, 11]
    else:
        workdf.iloc[i, 11] = i
print("truncated final_DH with partids column: {}".format(workdf))


workdf.loc[:, 'dIsc'] = 0
for i in range(1, len(workdf.index)):
    index = workdf.iloc[i, 11]
    initvalue = workdf.iloc[index, 3]
    workdf.iloc[i, 12] = (workdf.iloc[i, 3] - initvalue) / initvalue * 100
workdf.loc[:, 'dVoc'] = 0
for i in range(1, len(workdf.index)):
    index = workdf.iloc[i, 11]
    initvalue = workdf.iloc[index, 4]
    workdf.iloc[i, 13] = (workdf.iloc[i, 4]-initvalue) / initvalue * 100
workdf.loc[:, 'dVmp'] = 0
for i in range(1, len(workdf.index)):
    index = workdf.iloc[i, 11]
    initvalue = workdf.iloc[index, 5]
    workdf.iloc[i, 14] = (workdf.iloc[i, 5] - initvalue) / initvalue * 100
workdf.loc[:, 'dImp'] = 0
for i in range(1, len(workdf.index)):
    index = workdf.iloc[i, 11]
    initvalue = workdf.iloc[index, 6]
    workdf.iloc[i, 15] = (workdf.iloc[i, 6] - initvalue) / initvalue * 100
workdf.loc[:, 'dPmp'] = 0
for i in range(1, len(workdf.index)):
    index = workdf.iloc[i, 11]
    initvalue = workdf.iloc[index, 7]
    workdf.iloc[i, 16] = (workdf.iloc[i, 7] - initvalue) / initvalue * 100
workdf.loc[:, 'dFF'] = 0
for i in range(1, len(workdf.index)):
    index = workdf.iloc[i, 11]
    initvalue = workdf.iloc[index, 8]
    workdf.iloc[i, 17] = (workdf.iloc[i, 8] - initvalue) / initvalue * 100
workdf.loc[:, 'dEff'] = 0
for i in range(1, len(workdf.index)):
    index = workdf.iloc[i, 11]
    initvalue = workdf.iloc[index, 9]
    workdf.iloc[i, 18] = (workdf.iloc[i, 9] - initvalue) / initvalue * 100

workdf["TimeSpent"] = 0
for i in range(0, len(workdf.index)):
    Sample = workdf.iloc[i, 2]
    if Sample.find('100') != -1:
        workdf.iloc[i, 19] = 100
    elif Sample.find('75') != -1:
        workdf.iloc[i, 19] = 75
    elif Sample.find('50') != -1:
        workdf.iloc[i, 19] = 50
    elif Sample.find("25") != -1:
        workdf.iloc[i, 19] = 25
    else:
        pass
print(workdf)


fig = make_subplots(rows=3, cols=2, subplot_titles=("dIsc",
                                                    "dVoc",
                                                    "dVmp",
                                                    "dImp",
                                                    "dPmp",
                                                    "dFF"))


#now inside of this for loop, it splits the workdf into its respective (partids)/(tested parts)
#it loops through to collect all same partids and add the index to a dummy list
#and when it reaches a value is not the same part id, then it finally plots that collected iv data, and reinitializes dummy list for next group

values = [0,1,2,3,4] ##for NJW0003
#values = [5,6,7,8,9] ##for NJW0005
#values = [10,11,12,13,14] ##for JW0007
#values = [15,16,17,18,19] ##for NJW0015

fig.append_trace(go.Scatter(
        x=workdf.iloc[values, 19], y=workdf.iloc[values, 12], text=workdf.iloc[values, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="lines+markers"
        ), row=1, col=1)  # Isc
fig.append_trace(go.Scatter(
        x=workdf.iloc[values, 19], y=workdf.iloc[values, 14], text=workdf.iloc[values, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="lines+markers"
        ), row=1, col=2)  # Voc

fig.append_trace(go.Scatter(
        x=workdf.iloc[values, 19], y=workdf.iloc[values, 15], text=workdf.iloc[values, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="lines+markers"
        ), row=2, col=1)  # Vmp

fig.append_trace(go.Scatter(
        x=workdf.iloc[values, 19], y=workdf.iloc[values, 16], text=workdf.iloc[values, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="lines+markers"
        ), row=2, col=2)  # Imp

fig.append_trace(go.Scatter(
        x=workdf.iloc[values, 19], y=workdf.iloc[values, 17], text=workdf.iloc[values, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="lines+markers"
        ), row=3, col=1)  # Pmp

fig.append_trace(go.Scatter(
        x=workdf.iloc[values, 19], y=workdf.iloc[values, 18], text=workdf.iloc[values, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="lines+markers"
        ), row=3, col=2)  # dFF
#values = [z+1]



fig.update_layout(height=500, width=1200,
                  title_text="Scatterplots of electrical parameters versus hours in HAST NJW-22-0006")
fig.update_annotations(font_size=12)
fig.update_yaxes(range=[0, 1], dtick=0.2)
for ax in fig['layout']:
    if ax[:5] == 'xaxis':
        fig['layout'][ax]['dtick'] = 25

fig.show()
