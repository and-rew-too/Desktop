import numpy as np
import pandas as pd


data = [
'Z12.700 ' ,
'G1Z-1.270F203.2 ' ,
'X120.000Y174.000F508.0 ' ,
'X162.000Y72.000 ' ,
'X60.000Y156.000 ' ,
'X192.000Y144.000 ' ,
'X66.000Y72.000 ' ,
'Z-2.540F203.2 ' ,
'X120.000Y174.000F508.0 ' ,
'X162.000Y72.000 ' ,
'X60.000Y156.000 ' ,
'X192.000Y144.000 ' ,
'X66.000Y72.000 ' ,
'Z12.700 ' ,
'M02 ' ]
#testing github 0909

df = pd.DataFrame(data, columns = ['Name'])
print(df)
coords = df["Name"].str.split("X", n = 1, expand = True)
df["xpos"] = coords[1]
df["xpos"] = df["xpos"].str.slice(0,6)
coords = df["Name"].str.split("Y", n = 1, expand = True)
df["ypos"] = coords[1]


df['all'] = 'Line ' + df['xpos'] + '#' + df['ypos'] + '# ' + '250#ON#Valid#30'
#df['A'] = '#'
print(df)
