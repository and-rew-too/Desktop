import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#THIS IS MOST IMPORTANT VARIABLE, CHANGES THE WAFER BEING LOOKED AT
start = 42  # 14,21,28,35

sheet_url = "https://docs.google.com/spreadsheets/d/1MJoo_LZrhD4qlF2OCJEpl-r85inmDwYIydU-xvpqWhc/edit#gid=1050225185"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)

YDAT = df.iloc[start:start+4, 3]
XDAT = df.iloc[start:start+4, 0]

plt.scatter(XDAT, YDAT, label="Real Print Diameter")
plt.legend(loc="lower right")

plt.title('Print Accuracy from Mean')
plt.xlabel('Print Speed')
plt.ylabel('Diameter smaller [mm]')
plt.ylim([-100, -0])
plt.grid()
plt.show()
