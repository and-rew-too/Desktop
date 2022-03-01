import math


T = 22
#temperature in C
V = .85
#MILLIVOLTS MEASURED OVERALL

# S is the Sensitivity before any temp calibration
# Scal = (0.00334*T + 0.917) * S
# 0.001136 mV / (W/m2)
Scal = (0.00334*T + 0.917) * 0.001136


HF = V/Scal
print(HF)
