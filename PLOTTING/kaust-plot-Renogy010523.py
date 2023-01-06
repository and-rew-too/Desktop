import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sheet_url = "https://docs.google.com/spreadsheets/d/1PzKvxN1ARlnQVYnCtM05Cs15VzTi76UHMyJmk6CQrNs/edit#gid=1504840331"
pd.set_option('display.width', None)
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)
print(df)


COL = 7 #3 is isc, 4 is voc, 7 is pmp, 8 s ff, 12 is pff, 13 is peff
column_headers = df.columns.values.tolist()
param = column_headers[COL]
plt.ylabel('{}'.format(param))
plt.xlabel('Hours in Damp Heat')
plt.title('{} As a function'.format(param))



def my_function(St,Modulenum):
    Xt = df.iloc[St:St + 6, 2]  # hours in damp heat
    Yt = df.iloc[St:St + 6, COL]  # electrical parameter
    print(Yt)

    plt.plot(Xt, Yt, marker="o",label=Modulenum)
my_function(0,"0001")
my_function(6,"0002")
my_function(12,"0003")
my_function(18,"0004")
my_function(24,"0005")
my_function(30,"0006")
my_function(36,"0007")
my_function(42,"0008")
my_function(48,"0009")


#Xt = df.iloc[St:St+5,2] #hours in damp heat
#Yt = df.iloc[St:St+5,COL] #electrical parameter
#print(Yt)


#plt.plot(Xt, Yt, label="Module 0001")
#plt.scatter(Xt, Yt, alpha=0.5)
plt.legend(loc="lower left")
plt.grid()
plt.show()
