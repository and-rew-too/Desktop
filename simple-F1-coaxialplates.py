import numpy as np

W1 = 25 #dimensions of active area for heat flux sensor 25mm
W2 = 160 #dimensions of square cell being tested, 166 mm by 166 mm
H = 100


w1 = W1/H
w2 = W2/H


a = w2-w1 #this stands for x
b = w2+w1 #this stands for y

u = np.sqrt(a**2+4)
v = np.sqrt(b**2+4)
s = u*(a*np.arctan(a/u)-b*np.arctan(b/v))
t = v*(b*np.arctan(a/u)-b*np.arctan(b/v))


F12 = (1/(np.pi*w1**2) * ( np.log((w1**2+w2**2+2)**2 )/ ( (a**2+2)*(b**2+2) )      + s - t)
print(F12)
