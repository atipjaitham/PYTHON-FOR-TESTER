# break: break out from nearest enclosing loop
# continue : Go to the start of nearest enclosing loop

x = 0
# y = 0
while x <= 10:
    print(x)
    x = x + 1
    # print("Parent While")
    # while y < 5:
    #     y = y + 1
    #     print(y)
    #     continue
    #     print("inner loop")
    if x == 5:
        break
else:
    print("out of while loop")