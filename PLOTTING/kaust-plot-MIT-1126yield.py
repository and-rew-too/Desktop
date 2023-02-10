
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#for meausrements of Voc, pFF, FF based on different heating profiles of huasun hjt cells
sheet_url = "https://docs.google.com/spreadsheets/d/17Bj5YxTy1Il1dnCcYDNoQw7MmK9QKrd0FsRSRyRZDY8/edit#gid=0"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)


Projectboolean = df.loc[df['Month']!=12]
#Projectboolean = df[~df['Month'].str.contains(MonthLooking)]
df.drop(Projectboolean.index, inplace=True)
print(df.iloc[:,1])
LEN = len(df.index)
x = np.linspace(0, LEN-1, LEN)
#print(x)
df.loc[df['DHI*COS(AOI)R1R2']<0,'DHI*COS(AOI)R1R2']=0 # ths is 34, area 36
df.loc[df['DHI*COS(AOI)T1']<0,'DHI*COS(AOI)T1']=0 # this is 35, area 27
df.loc[df['DHI*COS(AOI)T2']<0,'DHI*COS(AOI)T2']=0 # this is 36, area 17
df.loc[df['DHI*COS(AOI)TR1']<0,'DHI*COS(AOI)TR1']=0 # this is 37, area 78
df.loc[df['DHI*COS(AOI)TR2']<0,'DHI*COS(AOI)TR2']=0 # this is 38, area 44

print(sum(df.iloc[:,34]*0.2*0.036))
print(sum(df.iloc[:,35]*0.2*0.027))
print(sum(df.iloc[:,36]*0.2*0.017))
print(sum(df.iloc[:,37]*0.2*0.078))
print(sum(df.iloc[:,38]*0.2*0.044))

exit()

plt.plot(x, df.iloc[:,34] * 0.2 * 0.036, 'b--',label="R section")
plt.plot(x, df.iloc[:,35] * 0.2 * 0.027, 'chocolate',label="T1 section")
plt.plot(x, df.iloc[:,36] * 0.2 * 0.017, 'gold',label="T2 section")
plt.plot(x, df.iloc[:,37]*0.2 * 0.078, 'orangered',label="TR1 section")
plt.plot(x, df.iloc[:,38]*0.2 * 0.044, 'orange',label="TR2 section")
plt.legend(loc="lower left")
plt.title(r'Energy Yield For June $\gamma=0$')
plt.ylabel('Energy Yield (kWh / hr)')
plt.grid()
plt.show()
