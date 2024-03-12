# Positional Arguments
# Keyword Arguments
# Required Arguments
# Optional Arguments

def sub_demo(x=5,y=4): # x,y is parameter
    return x-y

z = sub_demo() #number in this is arguments
print(z)
print(sub_demo(10,6))
print(sub_demo(6))
print(sub_demo())
print(sub_demo(y=10))