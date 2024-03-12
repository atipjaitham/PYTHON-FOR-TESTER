f = open("writedemo.txt", "r+")
print(f.read())
f.close()

print(f.readline())
print(f.readline())
f.close

f = open("writedemo.txt", "a")
f.write("Some Contents, Some Contents, Some Contents, Some Contents, Some Contents, Some Contents")
f.close