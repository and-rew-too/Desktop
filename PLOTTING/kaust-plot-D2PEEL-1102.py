import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=1320437860"
url_1 = sheet_url.replace('/edit#gid=' , '/export?format=csv&gid=')
df = pd.read_csv(url_1,)

plt.plot(df.iloc[:,0], df.iloc[:,1], 'k',label="ABF-58Q Soldered to Luvata")
plt.plot(df.iloc[:,0], df.iloc[:,2], 'k',linestyle='--', label="ABF-58Q Soldered to Luvata")
plt.plot(df.iloc[:,0], df.iloc[:,3], 'b',label="Sunpreme CA-183 and Ulbrich")
plt.plot(df.iloc[:,0], df.iloc[:,4], 'b',linestyle='--', label="Sunpreme CA-183 and Ulbrich")
plt.plot(df.iloc[:,0], df.iloc[:,5], 'r',label="Huasun CA-183 and Ulbrich")
plt.plot(df.iloc[:,0], df.iloc[:,6], 'r',linestyle='--', label="Huasun CA-183 and Ulbrich")

plt.legend(loc="upper right")

plt.xlabel('Extension [mm]')
plt.ylabel('Load/Width [N/mm]')
plt.grid()
plt.show()
