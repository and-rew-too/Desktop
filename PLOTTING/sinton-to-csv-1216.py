import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width', None)
peelcsv = "C:/Users/andre/Downloads/CEC1-21-0110-0005.txt"
df = pd.read_csv(peelcsv, sep = '\t')
df = pd.read_csv(peelcsv, sep = '\t')
#Extrazeros = df[df.iloc[:, 0] <= 0.001].index
#df.drop(Extrazeros, inplace=True)

df = df.sort_values('Vload_(V)', ascending=False)
print(df)

svocdf = df.sort_values('SunsVoc_Voltage_(V)', ascending=True)
Extrazeros = svocdf[svocdf.iloc[:, 4] <= 0.2].index
svocdf.drop(Extrazeros, inplace=True)
plt.plot(df.iloc[:,0],df.iloc[:,1],label="Sunpower Me-3 Full")
plt.plot(svocdf.iloc[:,3],svocdf.iloc[:,4],label="SunsVoc")
plt.ylim([0, 3])
plt.xlim([0, 1.8])
plt.grid()
plt.show()