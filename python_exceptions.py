try:
    print("Input first number: ")
    x = int(input())
    print("Input second number: ")
    y = int(input())
    if x == 0 or y == 0:
        raise Exception("The denominator is 0")
    print(x/y)
except Exception as e:
    print(e)
    print("In except block")
else:
    print("In else block")
finally:
    print("This is always executed")

# Input first number: 
# 3
# Input second number:
# 3
# 1.0
# In else block
# This is always executed50