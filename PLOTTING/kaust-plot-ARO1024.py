import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=569396914"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)
part = df
column_headers = df.columns.values.tolist()



plt.figure(figsize=(13,8)) #deactive this to have all figures in individual plots
for i in range(1,12,2):
    y = df.iloc[0:21,i+1]
    y = y/25 #converts from N to N/mm
    plt.plot(df.iloc[0:21,i], y, label = column_headers[i])
plt.legend(loc="lower right")
plt.title('Fit Plot for Sequential T-Peel Testing')
plt.xlabel('Extension (mm)')
plt.ylabel('Peel Strength (N/mm)')
plt.grid()
#plt.savefit("ARO1024.png")
plt.show()
