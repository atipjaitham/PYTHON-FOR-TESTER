demo_set1 = {"Delhi", "Kolkata", "Melbourne", "Sydney"}
demo_set2 = {"Delhi", "Kolkata", "Melbourne", "Sydney", "New York", "Bangkok"}
# add(elem) - Add element elem to the set.
# remove(elem) - Remove element elem from the set. Raises KeyError if elem is not contained in the set.
# discard(elem) - Remove element elem from the set if it is present.
# pop() - Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
# clear() - Remove all elements from the set.
print(demo_set1)
demo_set1.add("Taipei")
print(demo_set1)
demo_set1.remove("Delhi")
print(demo_set1)
demo_set1.pop()
demo_set1.clear()
print(demo_set1)

#Joining two sets
# union()
# update()
demo_set3 = demo_set1.union(demo_set2)
print(demo_set1)
demo_set1.update(demo_set2)
print(demo_set1)

#intersection(demo_set2)
demo_set3 = demo_set1.intersection(demo_set2)
print (demo_set3)
demo_set1.intersection_update(demo_set2)
print (demo_set1)

#symmetric_difference()
# will be print data that diffetance
demo_set3 = demo_set1.symmetric_difference(demo_set2)
print (demo_set3)
demo_set1.symmetric_difference_update(demo_set2)
print (demo_set1)
# differance
demo_set3 = demo_set2.difference(demo_set1)
print (demo_set3)
demo_set2.difference_update(demo_set1)
print (demo_set2)

#issubset()
z = demo_set1.issubset(demo_set2)
print (z)
#issuperset()
z = demo_set2.issuperset(demo_set1)
print (z)