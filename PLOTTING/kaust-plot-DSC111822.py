import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


directory = "C:/Users/andre/Downloads/20min130.txt"
pd.set_option('display.width', None)
dfL130 = pd.read_csv("C:/Users/andre/Downloads/POETR01BA-gel-20min155C-111722.txt", names=['Temp','Time','Response','Sens.'], skiprows=38, sep='\;', engine='python')
control = pd.read_csv("C:/Users/andre/Downloads/POETR01BA-gel-uncured-111722.txt", names=['Temp','Time','Response','Sens.'], skiprows=38, sep='\;', engine='python')

LSIDE = 2100
RSIDE = 2300 #THIS IS FROM 88.9 c TO 96 c
print(sum(dfL130.iloc[LSIDE:RSIDE,2])/200)

L130shift = sum(dfL130.iloc[LSIDE:RSIDE,2])/(200)
# M130shift = sum(dfM130.iloc[LSIDE:RSIDE,2])/(200)
# S130shift = sum(dfS130.iloc[LSIDE:RSIDE,2])/(200)
# L145shift = sum(dfL145.iloc[LSIDE:RSIDE,2])/(200)
# M145shift = sum(dfM145.iloc[LSIDE:RSIDE,2])/(200)
# S145shift = sum(dfS145.iloc[LSIDE:RSIDE,2])/(200)
# L155shift = sum(dfL155.iloc[LSIDE:RSIDE,2])/(200)
# M155shift = sum(dfM155.iloc[LSIDE:RSIDE,2])/(200)
# S155shift = sum(dfS155.iloc[LSIDE:RSIDE,2])/(200)
controlshift = sum(control.iloc[LSIDE:RSIDE,2])/(200)

dfL130['Response'] = dfL130['Response'] + abs(L130shift) + 0.03
# dfM130['Response'] = dfM130['Response'] + abs(M130shift)
# dfS130['Response'] = dfS130['Response'] + abs(S130shift)
# dfL145['Response'] = dfL145['Response'] + abs(L145shift)
# dfM145['Response'] = dfM145['Response'] + abs(M145shift)
# dfS145['Response'] = dfS145['Response'] + abs(S145shift)
# dfL155['Response'] = dfL155['Response'] + abs(L155shift)
# dfM155['Response'] = dfM155['Response'] + abs(M155shift)
# dfS155['Response'] = dfS155['Response'] + abs(S155shift)
#MANUAL CORRECTION VALUE HERE
manualshift =  0.0
control['Response'] = control['Response'] + abs(controlshift) - manualshift


Ltemp = 2300
Rtemp = 5300 # AREA UNDER CURVE FROM 143C - 186C #5300 is area from 143 to 200

#initializing values below
VALUE155 = 0
control25 = 0
for i in range(Ltemp,Rtemp):
    Astep = 0.5*(dfL130.iloc[i+1,2]+dfL130.iloc[i,2]) * ( dfL130.iloc[i+1,0]-dfL130.iloc[i,0] )
    VALUE155 = VALUE155+Astep
    #intermediate steps inbewteen
    jstep = 0.5*(control.iloc[i+1,2]+control.iloc[i,2]) * ( control.iloc[i+1,0]-control.iloc[i,0] )
    control25 = control25+jstep
area = pd.DataFrame(np.array([VALUE155, control25]))
cure = pd.DataFrame(np.array([0,0]))
print(area)


#plt.plot(dfL130.iloc[Ltemp:Rtemp,0], control.iloc[Ltemp:Rtemp,2], alpha=0.5, label="Uncured Value")
#plt.plot(dfL130.iloc[Ltemp:Rtemp:,0], dfL130.iloc[Ltemp:Rtemp,2], alpha=0.5, label="Cured data")
plt.plot(dfL130.iloc[Ltemp:Rtemp,0], control.iloc[Ltemp:Rtemp,2], alpha=0.5, label="Uncured Value")
plt.plot(dfL130.iloc[Ltemp:Rtemp:,0], dfL130.iloc[Ltemp:Rtemp,2], alpha=0.5, label="Cured data")
plt.grid()
plt.show()
