import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


sheet_url = "https://docs.google.com/spreadsheets/d/1MJoo_LZrhD4qlF2OCJEpl-r85inmDwYIydU-xvpqWhc/edit#gid=1203996951"
url_1 = sheet_url.replace('/edit#gid=' , '/export?format=csv&gid=')
val = pd.read_csv(url_1,)
pd.set_option('display.width', None)
df = pd.read_csv(url_1,)



#df2 = pd.DataFrame(T, columns = ['Column_A'])
#creating the linear regression line based off measured values
Xext = np.linspace(14, 24, 21)
df2 = pd.DataFrame(Xext, columns = ['A'])
Yext = 6.347*Xext +26.758
df2['B'] = Yext

Xext1 = np.linspace(0, 14, 15)
Yext1 = 6.347*Xext1 +26.758
# insert this into same pandas dataframe to plot later, but unnecessary
# df = df.append(df2)
# print(df)


plt.plot(Xext1, Yext1, 'k',label="Fitted Curve")
plt.plot(Xext, Yext, 'k--',label="Extrapolated Curve")
plt.scatter(df.iloc[0:8,1], df.iloc[0:8,3], alpha=0.5, label="Experimental Data")
plt.legend(loc="lower right")

plt.title('Forward Bias Temperature - 36cell - 32mmx28mm')
plt.xlabel('Multiple of Isc')
plt.ylabel('Cell Temperature (C)')
plt.grid()
plt.show()
