import numpy as np
import pandas as pd

# cell parameters needed here
# busbarpitch = ??? currently set to 38.5
# celldimensions = 166mm for 9BB Jollywood
Power = 30  # not the module, the laser Power

# DATAFRAME START initial three rows of laser cuts
sdf = pd.DataFrame(np.zeros([3, 7])*np.nan)
sdf.iloc[0, 0:3] = 'Y-axis#', 0, 8.5-5  # CHANGED
sdf.iloc[1:3, 0:3] = 'X-axis#', 167, 0

# DATAFRAME MIDDLE
pd.set_option('display.width', None)
ROWS = 50
# 50 is excess will have NaN at the bottom
df = pd.DataFrame(np.zeros([ROWS, 7])*np.nan)


widths = pd.DataFrame([30, 25, 20, 15])
print(widths)

iloop = 0
numloop = (len(widths.index))

for j in range(0, numloop):
    #for j in range(0,4):
    for i in range(iloop, iloop+6):
        print(i)
        if (i+1) % 6 == 0:
            df.iloc[i, 0:3] = "Y-axis#", 0, 38.5-widths.iloc[i//6, 0]
        elif (i+1) % 3 == 0:
            df.iloc[i, 0:3] = "Y-axis#", 0, widths.iloc[i//6, 0]
        else:
            df.iloc[i, 0:3] = "X-axis#", 167, 0
    iloop = iloop + 6
# middle portion finished, very last row y-axis 9.6 is extra, and doesn't need to be cut
# code below goes through df, NaN rows get dropped, also the very last non-NaN y-axis value
is_NaN = df.isnull()
for kk in range(0, len(df.index)):
    if is_NaN.iloc[kk, 0] == True:
        df.drop(labels=kk-1, inplace=True)
    else:
        pass
df.drop(labels=0, inplace=True)  # first X-axis 0.0 row that isn't used
df.drop(labels=1, inplace=True)  # second X-axis 0.0 row that isn't used
df.drop(labels=ROWS-1, inplace=True)  # additional NaN row that isn't used


#DATAFRAME END
edf = pd.DataFrame(np.zeros([6, 7])*np.nan)
edf.iloc[0, 0:3] = 'X-axis#', 3.625, 0
edf.iloc[1, 0:3] = 'Y-axis#', 0, -135
edf.iloc[2, 0:3] = 'Y-axis#', 0, 135
edf.iloc[3, 0:3] = 'X-axis#', 167-8.25, 0
edf.iloc[4, 0:3] = 'Y-axis#', 0, -135
edf.iloc[5, 0:3] = 'Y-axis#', 0, 135


# compiles the start, middle, end into single dataframe
df = pd.concat([sdf, df, edf])
# takes col 1 values and turns the 167, 167 into 167 -167
for i in range(1, len(df.index)):
    if df.iloc[i-1, 1] == 167:
        df.iloc[i, 1] = -df.iloc[i, 1]
    else:
        pass
df.iloc[:, 3] = "400#"
df.iloc[:, 4] = "ON#"
df.iloc[:, 5] = "Valid#"
df.iloc[:, 6] = Power


df.iloc[:, 2] = df.iloc[:, 2].astype(str) + '#'
df.iloc[:, 1] = df.iloc[:, 1].astype(str) + '#'
print(df)
df = df.to_string(header=False, index=False)

#with open('C:/users/andre/Downloads/ncprgtest.txt', 'a') as f:
#    f.write(df)
