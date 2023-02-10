import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=1299744041"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
print(df)
workdf = df
COL =20 #incredibly important parameter must change this
#39 is pFF #40 pEff, #14 is Jsc #9 is Pmp #10 is FF #j01 is 43 #j02 is 44

column_headers = df.columns.values.tolist()
param = column_headers[COL]
# 1:6, 8:13, 15:20
fig = plt.figure(figsize=(6,9))

plt.plot(df.iloc[0:5,1], df.iloc[0:5,COL],'-o',label="Sunpower Me-3 Full")
plt.plot(df.iloc[7:12,1], df.iloc[7:12,COL],'-o',label="PERC Full")
plt.plot(df.iloc[14:19,1], df.iloc[14:19,COL],'-o',color='salmon',label="PERC Shingle")
plt.plot(df.iloc[21:26,1], df.iloc[21:26,COL],'-o',label="Sunpower Ke Full")




#plt.ylim(upper*0.75,upper+0.05*upper)


#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.2))

plt.legend(loc="upper left")
plt.xlabel('Irradiance Intensity (W/m2)')
plt.ylabel(param)
plt.title('Width performance of {}'.format(param))
plt.grid()
plt.show()
