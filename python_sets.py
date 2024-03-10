demo_set1 = {5, 10, 20, 20, 30, 30, 30, 40}
demo_set2 = {10, 20, "30", 40, 40.5}
demo_set3 = {"10", "30"}
demo_set4 = set(("45",45,"67",65)) # If use set() can't use {} for assign value

print(demo_set1)
print(demo_set4)
print(len(demo_set1)) # don't count the duplicate value

print("20" in demo_set1) # check membership