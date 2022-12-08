import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sheet_url = "https://docs.google.com/spreadsheets/d/17Bj5YxTy1Il1dnCcYDNoQw7MmK9QKrd0FsRSRyRZDY8/edit#gid=828671485"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)

plt.plot(df.iloc[0:12,0], df.iloc[0:12,1], "k--",label=r"$\gamma=0$")
plt.plot(df.iloc[0:12,0], df.iloc[0:12,2],"b--",label=r"$\gamma=60$")
plt.plot(df.iloc[0:12,0], df.iloc[0:12,3], "c--",label=r"$\gamma=120$")
plt.plot(df.iloc[0:12,0], df.iloc[0:12,4], "y--",label=r"$\gamma=180$")
plt.plot(df.iloc[0:12,0], df.iloc[0:12,5], "g--",label=r"$\gamma=240$")
plt.plot(df.iloc[0:12,0], df.iloc[0:12,6], "k",label=r"$\gamma=300$")
plt.plot(df.iloc[0:12,0], df.iloc[0:12,7], "m--",label=r"$\gamma=330$")


plt.legend(loc="upper left")
plt.title(r'Energy Yield (kWh/month) of varied $\gamma$')
plt.ylabel('Energy Yield (kWh/month)')
plt.xlabel('Month')
plt.ylim([0,9000])


plt.grid()
plt.show()
