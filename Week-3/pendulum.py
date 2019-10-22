# PENDULUM FORMULA !
L = int((input('What is the length of your pendulum ? ')))
g = int((input('Which value of g do you want me to input ? ')))

import math

def period(L, g):
    try:
        return 2*(math.pi)*((L/g)**(1/2))
    except TypeError:
        print('Your input has to be numerical.')
    except ValueError:
        print('The value that you have entered breaks this function.')
    except ZeroDivisionError:
        print('You can not divide by zero.')

print(period(L, g))
