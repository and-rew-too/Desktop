import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


sheet_url = "https://docs.google.com/spreadsheets/d/1MJoo_LZrhD4qlF2OCJEpl-r85inmDwYIydU-xvpqWhc/edit#gid=1050225185"


url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)

YREF = df.iloc[0:5,3]
start = 7 #14,28,35
YDAT = df.iloc[start:start+5,3]

XREF = df.iloc[0:5,0]
XDAT = df.iloc[0:5,0]




plt.plot(XREF, YREF, 'k',label="Expected Print Diameter")
plt.plot(XDAT, YDAT, 'k--',label="Real Print Diameter")
#plt.scatter(df.iloc[0:8,1], df.iloc[0:8,3], alpha=0.5, label="Experimental Data")
plt.legend(loc="lower right")
