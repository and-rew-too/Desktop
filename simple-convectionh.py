import math 
#https://www.desmos.com/calculator/j4lgpzpsn6

k = 0.025 #conductivity W/mK #conductivity of air
characteristiclength = 0.005

#h = Nu*l / k
#below will now be finding Nu
#the convection solving for here is a flat plate
#the convection is assumed to be forced, and laminar

#Re = 100000
Re = 50000 
Pr = 0.71 #material constant for fluids
Nu = (0.339*Re**(1/2)*Pr**(1/3))  /  ( 1+(0.0458/Pr)**(2/3) )**(1/4)

h = (Nu*characteristiclength) / k





