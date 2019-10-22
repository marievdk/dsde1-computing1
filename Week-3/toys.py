'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''
# Coding 

a = int(input("Input a number : "))
# write a function that adds 1
# to the input and prints the result
def inc(a):
    print(a+1)
print(inc(a))


# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    return(a+1) # hint this is incomplete
print(inc_return(a))

b = int(input("Input another number : "))
# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    return a+b
print(sum(a,b))


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    return inc_return(sum(a,b))

print(sum_inc(a,b))



# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
c = int(input("Input a last number : "))

def is_even(c): 
    if c%2 == 0 :
        return('True, that is an even number')
    else :
        return('False, that is an odd number')

print(is_even(c))        

    

# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    s=str()
    for XXX in range(repeat):
        s += phrase
    print(s)
print(string_repeat('ho', 3)


   

