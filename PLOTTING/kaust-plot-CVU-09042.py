import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


sheet_url = "https://docs.google.com/spreadsheets/d/1MJoo_LZrhD4qlF2OCJEpl-r85inmDwYIydU-xvpqWhc/edit#gid=1203996951"
url_1 = sheet_url.replace('/edit#gid=' , '/export?format=csv&gid=')
val = pd.read_csv(url_1,)
pd.set_option('display.width', None)
df = pd.read_csv(url_1,)

plt.scatter(df.iloc[0:8,1], df.iloc[0:8,3], alpha=0.5, label="Experimental Data - 32mmx28mm")
plt.scatter(df.iloc[6:8,1], df.iloc[6:8,4], alpha=0.5, label="Experimental Data - 32mmx39mm")
plt.legend(loc="lower right")

plt.title('Forward Bias Temperature')
plt.xlabel('Multiple of Isc')
plt.ylabel('Cell Temperature (C)')
plt.grid()
plt.show()
