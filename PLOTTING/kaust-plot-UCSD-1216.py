import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#for measurements of Voc, pFF, FF, based on different SAS cell etch depths and times
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=1579843966"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
workdf = df.iloc[:, [3, 4,5,6,7,8,9,10,11,12,13,14,20,21,39,40]]
print(workdf)
COL = 13 #incredibly important parameter must change this
# 123 is isc voc, 7 is ff, 12 is pff
Param = list(workdf.columns)[COL]
print(Param)

#x1 is SAS type C
#x3 is SAS type H
#x3 s huasun drilled mwt


#plt.boxplot([x for x in [x1, x2, x3]], 0, 'rs', 1)

# plt.xticks([y+1 for y in range(len([x1, x2, x3]))], ['ECA', 'MCCA', 'MCCA-DMSO'])
# plt.xlabel('Cell Group')
# plt.ylabel(Param)
# t = plt.title('Box plot of ' + Param)
# plt.grid()
# plt.show()

plt.rcParams['figure.figsize'] = [2.5, 5]

#fig = plt.figure(figsize=(2.5,7))
#plt.boxplot([x for x in [x0, x1, x2]], 0, 'rs', 1)
c = ['blue', 'cyan', 'cyan']
plt.bar(workdf.iloc[:,0], workdf.iloc[:,COL], color = c)
ylimdf = workdf.iloc[:,COL]
maximum = ylimdf.max()
Ymax = maximum + maximum*0.12
Ymin = maximum - maximum*0.95 #change to 2 for Rs

plt.xlabel('Conductive Adhesive Type')
plt.ylabel('Rs_(ohm-cm2)')
plt.ylim([Ymin, Ymax])
plt.xticks(rotation=8)



plt.show()