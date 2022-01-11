import plotly
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math

sheet_url = "https://docs.google.com/spreadsheets/d/1DlP7xF7aEk0xDsFkoAHK4fokn7nnX0AkwAXq0nBJSIs/edit#gid=0"
url_1 = sheet_url.replace('/edit#gid=' , '/export?format=csv&gid=')
val = pd.read_csv(url_1,)
pd.set_option('display.width', None)


q = 1.602*10**19
#LENGTH OF TRANSMISSION DATA IS 429
#len(df.index) = 429
df = pd.DataFrame(np.zeros([429,7]))
#column 2, for etfe ctrl
newdf = pd.DataFrame(np.zeros([429*5,9]))


set5 = 0
for i in range(0,len(val.index)):
    if math.isnan(val.iloc[i,4])==False:
        for j in range(set5,set5+5):
            newdf.iloc[j,3] = val.iloc[i,4]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end


#column 3, for pet ctrl
set5 = 0
for i in range(0,len(val.index)):
    if math.isnan(val.iloc[i,5])==False:
        for j in range(set5,set5+5):
            newdf.iloc[j,4] = val.iloc[i,5]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end
#column 4, for etfe hast
set5 = 0
for i in range(0,len(val.index)):
    if math.isnan(val.iloc[i,6])==False:
        for j in range(set5,set5+5):
            newdf.iloc[j,5] = val.iloc[i,6]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end
#column 5, for pet hast
set5 = 0
for i in range(0,len(val.index)):
    if math.isnan(val.iloc[i,7])==False:
        for j in range(set5,set5+5):
            newdf.iloc[j,6] = val.iloc[i,7]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end
#column 6, for etfe suv
set5 = 0
for i in range(0,len(val.index)):
    if math.isnan(val.iloc[i,9])==False:
        for j in range(set5,set5+5):
            newdf.iloc[j,7] = val.iloc[i,9]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end
#column 7, for pet suv
set5 = 0
for i in range(0,len(val.index)):
    if math.isnan(val.iloc[i,8])==False:
        for j in range(set5,set5+5):
            newdf.iloc[j,8] = val.iloc[i,8]
        set5 = set5+5
        #end
    else:
        continue
    #end
#end











newdf.iloc[:,0] = val.iloc[:,0]
newdf.iloc[:,1] = val.iloc[:,1]
newdf.iloc[:,2] = val.iloc[:,2]+val.iloc[:,3]

newdf.columns = ['wavelength','EQE - cougar','Flux - AM1.5',
                '125 ETFE CTRL','125 PET CTRL',
                '125 ETFE HAST12','125 PET HAST12',
                '125 ETFE SUV24','125 PET SUV24']
print(newdf)


fig = go.Figure()
fig.add_trace(go.Scatter(x=newdf.iloc[:,0], y=newdf.iloc[:,3],
                    mode='markers',
                    name='markers'))
fig.add_trace(go.Scatter(x=newdf.iloc[:,0], y=newdf.iloc[:,4],
                    mode='markers',
                    name='markers'))
fig.add_trace(go.Scatter(x=newdf.iloc[:,0], y=newdf.iloc[:,5],
                    mode='markers',
                    name='markers'))
fig.add_trace(go.Scatter(x=newdf.iloc[:,0], y=newdf.iloc[:,6],
                    mode='markers',
                    name='markers'))

fig.show()




# # base code to duplicate a row (n) this case (5) times into a new row
# set10 = 0
# newdf = pd.DataFrame(np.zeros([3*5,7]))
# for i in range(0,len(df.index)):
#     for j in range(set10,set10+5):
#         newdf.iloc[j,0] = df.iloc[i,0]
#     set10 = set10+5
# print(newdf)
