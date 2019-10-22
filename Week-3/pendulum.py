# PENDULUM FORMULA !
L = (input('What is the length of your pendulum ? '))
g = (input('Which value of g do you want me to input ? '))

import math

def period(L, g):
    return 2*math.pi*((L/g)**(1/2))

print(period(L, g))
