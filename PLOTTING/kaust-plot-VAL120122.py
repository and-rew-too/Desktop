import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=1727359835"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
print(df)

#my_array = np.array([[11,22,33],[44,55,66]])
x0 = df.iloc[:,0]
y0 = df.iloc[:,1]

plt.ylabel('W/kg')
plt.xlabel('Configuration')
plt.title('W/kg functon of Foam Milling')
plt.scatter(x0, y0, label="110um silicon")
plt.legend(loc="upper left")
plt.show()