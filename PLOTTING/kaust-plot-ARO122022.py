import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#for measurements of Voc, pFF, FF, based on different SAS cell etch depths and times
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=1794705851"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
print(df)


workdf = df
#workdf = df.iloc[:, [0, 1,2,3,4,5,6,7]]
#print(workdf)





COL = 9 #incredibly important parameter must change this #1, 9 ,10
#START3 FOR NEXT ROW is 0,9, 18, 27, 36
start3 = 9

if start3 == 0:
    Param = "Tedlar "
elif start3 == 9:
    Param = "Maxeon Front "
elif start3 == 18:
    Param = "Maxeon Rear "
elif start3 == 27:
    Param = "DSC "
elif start3 == 36:
    Param = "ECTFE "
elif start3 == 45:
    Param = "FEP "
else:
    Param = "nah"
column_headers = df.columns.values.tolist()
Param = Param+column_headers[COL]

#Param = "Maxeon Rear - HF5"

x1 = workdf.iloc[start3:start3+3,COL]
x2 = workdf.iloc[start3+3:start3+6,COL]
x3 = workdf.iloc[start3+6:start3+9,COL]

x4 = workdf.iloc[start3+5:start3+7,7]
x5 = workdf.iloc[start3+5:start3+7,7]
x6 = workdf.iloc[start3+5:start3+7,7]

print(workdf.iloc[start3+3:start3+6,COL])



fig = plt.figure(figsize=(12,9))
plt.boxplot([x for x in [x1, x2,x3]], 0, 'rs', 1)
#plt.boxplot([x for x in [x4,x5, x6]], 0, 'rs', 1)
plt.xticks([y+1 for y in range(len([x1, x2,x3]))], ['Starting Thickness', '2mil Thickness','1mil Thickness'])
plt.ylabel('Peel Strength [N/mm]')
t = plt.title('Box plot of ' + Param)
plt.ylim([0,5.5]) # 0 to 5.5
plt.grid()
plt.show()
