import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=1299744041"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
print(df)
workdf = df
COL = 11 #incredibly important parameter must change this
#39 is pFF #40 pEff, #14 is Jsc #9 is Pmp #10 is FF
#11 s eFF

column_headers = df.columns.values.tolist()
param = column_headers[COL]
# 1:6, 8:13, 15:20
fig = plt.figure(figsize=(10,9))

plt.scatter(df.iloc[1:5,1], df.iloc[1:5,COL],label="Sunpower Me-3 Full")
plt.scatter(df.iloc[8:12,1], df.iloc[8:12,COL],label="PERC Full")
plt.scatter(df.iloc[15:19,1], df.iloc[15:19,COL],label="PERC Shingle")
#plt.plot(df.iloc[:,1], df.iloc[:,COL], 'k',linestyle='--', label="ABF-58Q Soldered to Luvata")

plt.xlabel('Suns')
plt.ylabel(param)
plt.title('Width performance of {}'.format(param))
plt.grid()
plt.show()
