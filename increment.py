import numpy as np
n = 1543
numlength = 8

while divmod(n,10**numlength)[0] == 0:
    numlength = numlength - 1
print(numlength)

print(divmod(n,10**3))

num = []
greatbool = []
ncheck = n
for i in range(n,0,-1):
    ncheck = n
    for i in range(numlength,0,-1):
        digitbool = divmod(ncheck,10**i)[0] > divmod(ncheck,10**(i-1))[0]%10
        greatbool.append(digitbool)
        digit = divmod(ncheck,10**i)[0]
        ncheck = divmod(ncheck,10**i)[1]
        num.append(digit)
        #print(digit)
    if (not any(greatbool)) == True:
        print(greatbool)
        break
    num = []
    greatbool = []
    n = n-1
print(not any(greatbool))
print(n)