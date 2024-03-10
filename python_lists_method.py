cities = ["Delhi", "Mumbai","Mumbai","Melbourne", "Sydney", "Kolkata" ]
print(cities)
# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
cities.append("Lucknow")
# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
cities.insert(1,"Lucknow")
# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
cities.remove("Mumbai")
# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.
cities.pop(3)
# list.clear()
# Remove all items from the list. Equivalent to del a[:].
updatedlist = new_cities.clear()
print(updatedlist)
# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
print(cities.index("Melbourne"))
# list.count(x)
# Return the number of times x appears in the list.
print(cities.count("Mumbai"))
# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
cities.sort()
print(cities)
# list.reverse()
# Reverse the elements of the list in place.
cities.reverse()
print(cities)
# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].
new_cities = cities.copy()
updatedlist = new_cities.clear()
print(updatedlist)