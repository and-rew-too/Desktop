from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd

sheet_url = "https://docs.google.com/spreadsheets/d/1MJoo_LZrhD4qlF2OCJEpl-r85inmDwYIydU-xvpqWhc/edit#gid=2085436549"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
print(df)


workdf = df.iloc[:, [3, 4,5,6,7,8,9,10,11,12,13,14,39,40]]
print(workdf)

import matplotlib.pyplot as plt


COL = 4 #incredibly important parameter must change this

x0 = workdf.iloc[3,COL] # reference cell only use the best one
x1 = workdf.iloc[5:7,COL]
x2 = workdf.iloc[9:11,COL]
x3 = workdf.iloc[13:15,COL]
x4 = workdf.iloc[17:19,COL]
x5 = workdf.iloc[21:22,COL]
x6 = workdf.iloc[25,COL]
x7 = workdf.iloc[29:30,COL]



fig = plt.figure(figsize=(12,9))

plt.boxplot([x for x in [x0, x1, x2, x3, x4, x5,x6,x7]], 0, 'rs', 1)

plt.xticks([y+1 for y in range(len([x0, x1, x2, x3,x4, x5,x6,x7]))], ['CTRL','180C20MIN', '180C40MIN', '230C20MIN','230C40MIN','250C20MIN','250C40MIN','280C20MIN'])
plt.xlabel('Parameters')
plt.ylabel('pFF_(%)')
t = plt.title('Box plot of pFF_(%)')
plt.grid()
#plt.show()

plt.savefig('box_1.png')

import win32com.client as win32
import sys
PptApp = win32.Dispatch("Powerpoint.Application")
PptApp.Visible = True
PPtPresentation = PptApp.Presentations.Open(r'C:\Users\andre\Downloads\Test.pptx')
pptSlide = PPtPresentation.Slides.Add(1,11)
Pict1 = pptSlide.Shapes.AddPicture(FileName=r'C:\Users\andre\Desktop\box_1.png', LinkToFile=False, SaveWithDocument=True, Left=100, Top=100, Width=-1, Height=-1)
