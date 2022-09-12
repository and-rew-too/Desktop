import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#THIS IS MOST IMPORTANT VARIABLE, CHANGES THE WAFER BEING LOOKED AT
start = 28 #14,21,28,35

sheet_url = "https://docs.google.com/spreadsheets/d/1MJoo_LZrhD4qlF2OCJEpl-r85inmDwYIydU-xvpqWhc/edit#gid=1050225185"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)

YREF = df.iloc[0:5,3]
YDAT = df.iloc[start:start+5,3]

XREF = df.iloc[0:5,0]
XDAT = df.iloc[0:5,0]




XMEAN = pd.DataFrame(np.zeros([5,1]))
XMEAN = XMEAN + YDAT.mean()
print(df.iloc[0,3]-YDAT.mean())
plt.plot(XREF, YREF, 'k',label="Expected Print Diameter")
plt.plot(XDAT, YDAT, 'b',label="Real Print Diameter")
plt.plot(XDAT, XMEAN, 'b--',label="Mean Print Diameter")
plt.legend(loc="lower right")

plt.title('Print Accuracy for {}'.format(df.iloc[start,2]))
plt.xlabel('Print Hole Location')
plt.ylabel('Print Diameter [mm]')
plt.grid()
plt.show()
