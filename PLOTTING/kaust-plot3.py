import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



Length = 100 #cm
Width = 48 #cm
Area = Length*Width
print(Area)
print(Width/15.6)


exit()
###########Variables to Change#############
# enter the project ID no spaces, in this format 'AAA', if format includes
# AAA0 AAA9 Projstr will still read it
Projstr = 'CDG1'  # project ID
PARAMETER = 'dIsc'
# comments row, if left blank, is NaN, if filled is string df.iloc[:, 116]

###########like a museum Please Look but Do Not Touch ##############
pd.set_option('display.width', None)
df = pd.read_csv(
    "C:/Users/andre/Downloads/All-101521-Modules.csv")
df = df.sort_values(by = 'Measurement_Date-Time', ascending = False)

MindexNames = df[(df.iloc[:, 6] <= -0.1) | (
    df.iloc[:, 40] <= 0)].index
df.drop(MindexNames, inplace=True)
#condition to only choose a specific Batch_ID \ Project ID
projectboolean = df[~df['Batch_ID'].str.contains(Projstr)]
df.drop(projectboolean.index, inplace=True)

#nullboolean = df[df.iloc[:,116].isnull()]
#df.drop(nullboolean.index, inplace=True)
df.iloc[:,3] = df.iloc[:,3].fillna('')
df.iloc[:,116] = df.iloc[:,116].fillna('')

# duncan requested correct sigfigs for I(A)
for i in range(0, len(df.index)):
    b = df.iloc[i, 5]*100
    if b//1000 >= 1:
        c = 3
    elif b//100 >= 1:
        c = 2
    elif b//10 >= 1:
        c = 1
    else:
        c = 0
    df.iloc[i, 5] = df.iloc[i, 5].round(decimals=c)
for j in range(6, 9):
    df.iloc[:, j] = df.iloc[:, j].round(decimals=2)
for k in range(9, 12):
    df.iloc[:, k] = df.iloc[:, k].round(decimals=2)
for m in range(38, 41):
    df.iloc[:, m] = df.iloc[:, m].round(decimals=2)
pd.set_option('display.width', None)

#TCboolean = df[df.iloc[:,116].str.contains("TC100")]
#print(TCboolean)
#HASTboolean = df[df.iloc[:,116].str.contains("HAST200")]
#print(HASTboolean)
DHboolean = df[df.iloc[:,116].str.contains("DH1000")]
int_DH = []
for i in range(0,len(DHboolean.index)):
    str = DHboolean.iloc[i,3]
    str = str[3:]
    #print(str)
    for j in range(0,len(df.index)):
        samples = df.iloc[j,3]
        #print(Samples)
        if samples.find(str) != -1:
            int_DH.append(df.iloc[j,:])
        else:
            pass
final_DH = pd.concat(int_DH, axis=1)
final_DH = final_DH.transpose()
print(final_DH)









workdf = final_DH.iloc[:,[0,3,116,5,6,7,8,9,10,11,39]] #creates truncated df, very important we are using this now

#comment this shit out of this one bro.. head scratcher forreal
#so first creates a new column that will be filled
#looping through the length , started at second row
#it checks the top row, row above, to see if it was iv data created at a later or earlier date
#if the iv data was created at a earlier date e.g. (df.i-1,0 < df.i,0)
# that means that the data above is for the same part
# so if true, then index the new column as the same part id
#and if not true, then create a new index number, as a new part id
workdf.loc[:,'partid,loop'] = 0
for i in range(1,len(workdf.index)):
    if workdf.iloc[i-1,0].astype(int) < workdf.iloc[i,0].astype(int):
        workdf.iloc[i,11] = workdf.iloc[i-1,11]
    else:
        workdf.iloc[i,11] = i


workdf.loc[:,'dIsc'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,3]
    workdf.iloc[i,12] = (workdf.iloc[i,3] -initvalue) / initvalue *100
workdf.loc[:,'dVoc'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,4]
    workdf.iloc[i,13] = (workdf.iloc[i,4]-initvalue) / initvalue *100
workdf.loc[:,'dVmp'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,5]
    workdf.iloc[i,14] = (workdf.iloc[i,5] -initvalue) / initvalue *100
workdf.loc[:,'dImp'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,6]
    workdf.iloc[i,15] = (workdf.iloc[i,6] -initvalue) / initvalue *100
workdf.loc[:,'dPmp'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,7]
    workdf.iloc[i,16] = (workdf.iloc[i,7] -initvalue) / initvalue *100
workdf.loc[:,'dFF'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,8]
    workdf.iloc[i,17] = (workdf.iloc[i,8] -initvalue) / initvalue *100
workdf.loc[:,'dEff'] = 0
for i in range(1,len(workdf.index)):
    index = workdf.iloc[i,11]
    initvalue = workdf.iloc[index,9]
    workdf.iloc[i,18] = (workdf.iloc[i,9] -initvalue) / initvalue *100

workdf["TimeSpent"] = 0
for i in range(0, len(workdf.index)):
    Sample = workdf.iloc[i,2]
    if Sample.find('250') != -1:
        workdf.iloc[i,19] = 250
    elif Sample.find('500') != -1:
        workdf.iloc[i,19] = 500
    elif Sample.find("1000") != -1:
        workdf.iloc[i,19] = 1000
    else:
        pass


print(workdf.iloc[37:41,12])
print(workdf)
x=[workdf.iloc[37:41,19],workdf.iloc[33:37,19]]
y=[workdf.iloc[37:41,12],workdf.iloc[33:37,12]]




#PARAMETER = 'dIsc' line 10 IS WHERE YOU CHANGE PARAMETER
groups = workdf.groupby('partid,loop')[PARAMETER].apply(list)
#print(groups)
xvals = []
enumerate_groups = enumerate(groups)
for i in range(0,len(groups)):
    iteration = next(enumerate_groups) # first iteration
    index, item = iteration
    xvals.append(item)
inddf = workdf.iloc[:,11].drop_duplicates()

Vocgroups = workdf.groupby('partid,loop')['dVoc'].apply(list)
Vocvals = []
enumerate_groups = enumerate(Vocgroups)
for i in range(0,len(Vocgroups)):
    iteration = next(enumerate_groups) # first iteration
    index, item = iteration
    Vocvals.append(item)

Impgroups = workdf.groupby('partid,loop')['dImp'].apply(list)
Impvals = []
enumerate_groups = enumerate(Impgroups)
for i in range(0,len(Impgroups)):
    iteration = next(enumerate_groups) # first iteration
    index, item = iteration
    Impvals.append(item)

Pmpgroups = workdf.groupby('partid,loop')['dPmp'].apply(list)
Pmpvals = []
enumerate_groups = enumerate(Pmpgroups)
for i in range(0,len(Pmpgroups)):
    iteration = next(enumerate_groups) # first iteration
    index, item = iteration
    Pmpvals.append(item)




fig, axs = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle("Change In Electrical Parameter after Damp Heat")

colors=['#00688b','#03a89e','#cd3700','#f9d84a','#ff6103','#00688b'
,'#03a89e','#cd3700','#f9d84a','#ff6103','#00688b','#03a89e','#cd3700','#f9d84a','#ff6103']
for i in range(10,len(groups)):
    indnum = inddf.iloc[i]
    axs[0].plot([0,250,500,1000], xvals[i],colors[i], label=workdf.iloc[indnum,1] )
    plt.legend(loc="upper right")
    axs[0].set_title('Isc')

for i in range(10,len(groups)):
    indnum = inddf.iloc[i]
    axs[1].plot([0,250,500,1000], Impvals[i],colors[i], label=workdf.iloc[indnum,1] )
    plt.legend(loc="upper right")
    axs[1].set_title('Imp')


for i in range(10,len(groups)):
    indnum = inddf.iloc[i]
    axs[2].plot([0,250,500,1000], Pmpvals[i],colors[i], label=workdf.iloc[indnum,1] )
    plt.legend(loc="upper right")
    axs[2].set_title('Pmp')



axs[2].set_xlabel('No. of Hours')
#ax = plt.axes()
for i  in range(0,3):
    axs[i].plot([0, 1000], [-0.5, -0.5], color="red", linestyle='--', dashes=(1, 2))
    axs[i].plot([0, 1000], [0, 0], color="black", linestyle='--', dashes=(1, 2))
    axs[i].plot([0, 1000], [0.5, 0.5], color="red", linestyle='--', dashes=(1, 2))
    axs[i].grid()
    axs[i].set_yticks([3,2,1,0,-1,-2,-3])
#ax.set_xlabel('No. of Hours')
#ax.set_ylabel('Percentage change in ' + PARAMETER)
plt.show()
