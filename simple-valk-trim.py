import numpy as np
import pandas as pd

###########like a museum Please Look but Do Not Touch ##############
pd.set_option('display.width', None)
df = pd.read_csv(
    "C:/Users/Andrew Hu/Dropbox/PC/Downloads/Valkyrie IV data for cleaning.csv")
df = df.sort_values(by='Measurement_Date-Time', ascending=True)
#df['Measurement_Date-Time'] = pd.to_datetime(df['Measurement_Date-Time'], format='%d-%b-%y')

print(df.iloc[41,3] == df.iloc[44,3])
#print(df.iloc[65:85,0:10])

# int_DH = []
# for i in range(1,len(df.index)):
#     if df.iloc[i,3] == df.iloc[i-1,3]:
#         if df.iloc[i,0] <= df.iloc[i-1,0]:
#             int_DH.append(df.iloc[i-1, :])
#         else:
#             pass
#     else:
#         pass

# int_DH = []
# for i in range(1,len(df.index)):
#     if df.iloc[i,0] <= df.iloc[i-1,0]:
#         int_DH.append(df.iloc[i-1, :])
#     else:
#         pass
#
# for i in range(1,len(df.index)-1):
#     if (df.iloc[i,3]!=df.iloc[i-1,3]) & (df.iloc[i+1,3]!=df.iloc[i,3]) :
#         int_DH.append(df.iloc[i, :])
#     else:
#         pass
# final_DH = pd.concat(int_DH, axis=1)
# final_DH = final_DH.transpose()
newdf = df.drop_duplicates(subset=['Sample_ID'], keep='last')
print(newdf)
newdf.to_csv('C:/Users/Andrew Hu/Downloads/trim-valk.csv', sep=',')
