import chart_studio.tools as tls
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd

###########Variables to Change#############
# enter the project ID no spaces, in this format 'AAA', if format includes
Projstr = 'D2'  # project ID
# comments row, if left blank, is NaN, if filled is string df.iloc[:, 116]

###########like a museum Please Look but Do Not Touch ##############
pd.set_option('display.width', None)


sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=1738090655"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
df = df.sort_values(by='Measurement_Date-Time', ascending = False)

MindexNames = df[(df.iloc[:, 6] <= -0.1) | (
    df.iloc[:, 40] <= 0)].index
df.drop(MindexNames, inplace=True)
#condition to only choose a specific Batch_ID \ Project ID
projectboolean = df[~df['Batch_ID'].str.contains(Projstr)]
df.drop(projectboolean.index, inplace=True)

#nullboolean = df[df.iloc[:,116].isnull()]
#df.drop(nullboolean.index, inplace=True)
df.iloc[:,3] = df.iloc[:,3].fillna('')
df.iloc[:,116] = df.iloc[:,116].fillna('')

# duncan requested correct sigfigs for I(A)
for i in range(0, len(df.index)):
    b = df.iloc[i, 5]*100
    if b//1000 >= 1:
        c = 5
    elif b//100 >= 1:
        c = 4
    elif b//10 >= 1:
        c = 3
    else:
        c = 2
    df.iloc[i, 5] = df.iloc[i, 5].round(decimals=c)
for j in range(6, 9):
    df.iloc[:, j] = df.iloc[:, j].round(decimals=3)
for k in range(9, 12):
    df.iloc[:, k] = df.iloc[:, k].round(decimals=3)
for m in range(38, 41):
    df.iloc[:, m] = df.iloc[:, m].round(decimals=3)
pd.set_option('display.width', None)

#TCboolean = df[df.iloc[:,116].str.contains("TC100")]
#print(TCboolean)
#HASTboolean = df[df.iloc[:,116].str.contains("HAST200")]
#print(HASTboolean)
DHboolean = df[df.iloc[:,116].str.contains("TC-200")]
#print(DHboolean)


int_DH = []
for i in range(0,len(DHboolean.index)):
    str = DHboolean.iloc[i,3]
    str = str[3:]
    #print(str)
    for j in range(0,len(df.index)):
        samples = df.iloc[j,3]
        #print(Samples)
        if samples.find(str) != -1:
            int_DH.append(df.iloc[j,:])
        else:
            pass
final_DH = pd.concat(int_DH, axis=1)
final_DH = final_DH.transpose()
print(final_DH)





workdf = final_DH.iloc[:,[0,3,116,5,6,7,8,9,10,11,39]] #creates truncated df, very important we are using this now

print(workdf)
#exit()

#comment this shit out of this one bro.. head scratcher forreal
#so first creates a new column that will be filled
#looping through the length , started at second row
#it checks the top row, row above, to see if it was iv data created at a later or earlier date
#if the iv data was created at a earlier date e.g. (df.i-1,0 < df.i,0)
# that means that the data above is for the same part
# so if true, then index the new column as the same part id
#and if not true, then create a new index number, as a new part id
workdf.loc[:,'partid,loop'] = 0
for i in range(1,len(workdf.index)):
    if workdf.iloc[i-1,0].astype(int) < workdf.iloc[i,0].astype(int):
        workdf.iloc[i,11] = workdf.iloc[i-1,11]
    else:
        workdf.iloc[i,11] = i


workdf.loc[:,'dIsc'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,3]
    workdf.iloc[i,12] = (workdf.iloc[i,3] -initvalue) / initvalue *100
workdf.loc[:,'dVoc'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,4]
    workdf.iloc[i,13] = (workdf.iloc[i,4]-initvalue) / initvalue *100
workdf.loc[:,'dVmp'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,5]
    workdf.iloc[i,14] = (workdf.iloc[i,5] -initvalue) / initvalue *100
workdf.loc[:,'dImp'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,6]
    workdf.iloc[i,15] = (workdf.iloc[i,6] -initvalue) / initvalue *100
workdf.loc[:,'dPmp'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,7]
    workdf.iloc[i,16] = (workdf.iloc[i,7] -initvalue) / initvalue *100
workdf.loc[:,'dFF'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,8]
    workdf.iloc[i,17] = (workdf.iloc[i,8] -initvalue) / initvalue *100
workdf.loc[:,'dEff'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,9]
    workdf.iloc[i,18] = (workdf.iloc[i,9] -initvalue) / initvalue *100

workdf["TimeSpent"] = 0
for i in range(0, len(workdf.index)):
    Sample = workdf.iloc[i,2]
    if Sample.find('100') != -1:
        workdf.iloc[i,19] = 100
    elif Sample.find('200') != -1:
        workdf.iloc[i,19] = 200
    elif Sample.find("300") != -1:
        workdf.iloc[i,19] = 300
    elif Sample.find('400') != -1:
        workdf.iloc[i,19] = 400
    elif Sample.find("500") != -1:
        workdf.iloc[i,19] = 500
    elif Sample.find('600') != -1:
        workdf.iloc[i,19] = 600
    elif Sample.find("700") != -1:
        workdf.iloc[i,19] = 700
    elif Sample.find('800') != -1:
        workdf.iloc[i,19] = 800
    elif Sample.find("900") != -1:
        workdf.iloc[i,19] = 900
    elif Sample.find("1000") != -1:
        workdf.iloc[i,19] = 1000
    else:
        pass

print(workdf)
# str = projboolean.iloc[3,3]
# #Samples = df.iloc[650:700,3]
# Samples = df.iloc[675,3]
# print(str)
# print(Samples)
# print(Samples.find(str))
# oth = df[df.iloc[:,116].str.contains("DH250")]

fig = make_subplots(rows=3, cols=2, subplot_titles=("dIsc",
                                                    "dVoc",
                                                    "dImp",
                                                    "dVmp",
                                                    "dPmp",
                                                    "dFF"))

fig.append_trace(go.Scatter(
        x=workdf.iloc[:, 19], y=workdf['dIsc'], text=workdf.iloc[:, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=1, col=1)

fig.append_trace(go.Scatter(
        x=workdf.iloc[:, 19], y=workdf['dVoc'], text=workdf.iloc[:, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=1, col=2)

fig.append_trace(go.Scatter(
        x=workdf.iloc[:, 19], y=workdf['dImp'], text=workdf.iloc[:, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=2, col=1)

fig.append_trace(go.Scatter(
        x=workdf.iloc[:, 19], y=workdf['dVmp'], text=workdf.iloc[:, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=2, col=2)

fig.append_trace(go.Scatter(
        x=workdf.iloc[:, 19], y=workdf['dPmp'], text=workdf.iloc[:, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=3, col=1)

fig.append_trace(go.Scatter(
        x=workdf.iloc[:, 19], y=workdf['dFF'], text=workdf.iloc[:, 1], hovertemplate='<br>x:%{x}<br>y:%{y}<br>m:%{text}', mode="markers"
        ), row=3, col=2)
fig.update_layout(height=600, width=600,
                  title_text="Scatterplots of electrical parameters versus hours in Damp Heat")
fig.update_annotations(font_size=12)


workdf.to_csv(r'C:\Users\andre\Downloads\refmodule-122722.csv', sep=',')


