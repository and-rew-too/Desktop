import plotly.graph_objects as go
import numpy as np
import pandas as pd
#https://stackoverflow.com/questions/67963140/pandas-dataframe-creating-3d-surface-plots

pd.set_option('display.width', None)
df = pd.read_csv( ?????
    "")

irrmean = df["Imp_(A)"].mean()
print(irrmean)
#Pmp standard deviation
P1 = (df.iloc[:,9].sub(irrmean)).pow(2)
P2 = P1.sum()
irrStandDev = (P2 / len(df.index))**(1/2)



columnposition = ["Sample_ID"][-3:-1]
df["Row"] = columnposition.astype(float) #briefly converts to float for math operations
df["Col"] = columnposition.astype(float)
x = df["Row"]
y = df["Col"] 
#convert x into a simple np 1x6 array
#convert y into a simple np 1x10 array
for i in range(1:len(x.index)):
  for j in range(1:len(j,index)):
    exes = df[df['Sample_ID'].str.contains(i)]
    exes = exes[exes['Sample_ID'].str.contains(j)]
    z[i][j] = exes["Imp_(A)"]
#convert the z values into something more meaningful like a 6x10 array 






# fig = go.Figure(data=[go.Surface(z=z_data.values)])
# fig.update_traces(contours_z=dict(show=True, usecolormap=True,
#                                   highlightcolor="limegreen", project_z=True))

# fig.update_layout(title='Mt Bruno Elevation', autosize=False,
#                   scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
#                   width=500, height=500,
#                   margin=dict(l=65, r=50, b=65, t=90)
# )
# fig.show()







