#tuples are indexed, allow duplicate values and cannot be modified (immutable)
demo_tuple = (1, 2, 3, 4, 5)
demo_tuple1 = ("Delhi", "Mumbai", "New York", "Melbourne", "Sydney")
demo_tuple2 = (True, False, False, True)
demo_tuple3 = (True, 1, "Delhi", 23.56)

print(len(demo_tuple2))
print(type(demo_tuple1))

print(demo_tuple1.count("Delhi"))
print(demo_tuple1.index("New York"))
print(demo_tuple2[0:2])

for x in demo_tuple1:
    print(x)

# #joint tuples
joined_turple = demo_tuple1 + demo_tuple2 + demo_tuple3
print(joined_turple)
print(type(joined_turple))