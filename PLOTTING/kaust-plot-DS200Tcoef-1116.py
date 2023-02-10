import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=749745277"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
#print(df)

#change iloc[HERE:HERE,]
COL = 3 #3 is isc, 4 is voc, 7 is pmp

St = 12
Xt = df.iloc[St:St+4,0]
Yt = df.iloc[St:St+4,COL]
print(Yt)

slope = np.polyfit(Xt,Yt,1) #slope[1] is slope, slope[2] is intercept
Coeff = (slope[0]*100)/(df.iloc[St,COL])
print(slope[0])
print(Coeff)

Xfit = np.linspace(10,60,41*10)
Yfit = Xfit*slope[0] + slope[1]


column_headers = df.columns.values.tolist()
param = column_headers[COL]
plt.ylabel('{}'.format(param))
plt.xlabel('Temperature (C)')
plt.title('{} As function of Temperature'.format(param))
plt.scatter(Xt, Yt, alpha=0.5, label="Experimental Tested Data")
plt.scatter(Xfit,Yfit,alpha=0.10, label="Line of best Fit")
plt.show()
plt.grid()
