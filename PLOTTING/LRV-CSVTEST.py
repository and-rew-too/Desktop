import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

peelcsv = "C:/Users/andre/Downloads/D2-22-SPWR3-SETUP.txt"
df = pd.read_csv(peelcsv, sep = '\t')

peel2csv = "C:/Users/andre/Downloads/D2-22-SPWR1-KE-RERE.txt"
df2 = pd.read_csv(peel2csv, sep = '\t')

peel3csv = "C:/Users/andre/Downloads/D2-22-LONGISHINGLE-1.txt"
df3 = pd.read_csv(peel3csv, sep = '\t')


#print(df.iloc[:,0])
plt.scatter(df.iloc[:,0],df.iloc[:,1],label="Sunpower Me-3 Full")
plt.scatter(df2.iloc[:,0],df2.iloc[:,1],label="Sunpower Ke Full")
plt.scatter(df3.iloc[:,0],df3.iloc[:,1],label="PERC full")


plt.ylim([0, 9])
plt.xlim([0, 0.8])
plt.grid()
plt.show()
