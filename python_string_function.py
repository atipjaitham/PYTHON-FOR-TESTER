x = "                       '::':''xyzatip jaitham      "
y= 123456789

# len(s): This function returns the length of the string s, i.e., the number of characters in the string.
print(len(x))
# str(): This function returns a string representation of the given object. If no argument is provided, it returns an empty string.
print(str(y))
z = str(y)
print(z.find("4567"))
# upper(): This function returns a copy of the string with all alphabetic characters converted to uppercase.
a = x.upper()
# count(sub[, start[, end]]): This function returns the number of non-overlapping occurrences of substring sub in the string. The search is done within the optional start and end indices.
print(x.count("a"))
# isupper(): This function returns True if all alphabetic characters in the string are uppercase, otherwise it returns False.
print(a.isupper())
# islower(): This function returns True if all alphabetic characters in the string are lowercase, otherwise it returns False.
print(a.islower())
# split(sep=None, maxsplit=-1): This function splits the string into a list of substrings, using the specified separator sep. If sep is not specified, any whitespace is a separator. The optional maxsplit argument specifies the maximum number of splits to do.
print(x.split())
# strip()
print(x.strip(':xyz \''))
# lstrip([chars]): This function returns a copy of the string with leading characters removed. If chars are given, it removes characters in chars from the left of the string. If chars is not provided, it removes leading whitespace.
print(x.lstrip(':xyz \''))
# rstrip([chars]): This function returns a copy of the string with trailing characters removed. If chars are given, it removes characters in chars from the right of the string. If chars is not provided, it removes trailing whitespace.
print(x.rstrip(':xyz \''))
# replace(old, new[, count]): This function returns a copy of the string with all occurrences of substring old replaced by new. If count is given, only the first count occurrences are replaced.
print(x.replace("xyz","golf",1))
# find(sub[, start[, end]]): This function returns the lowest index in the string where substring sub is found, or -1 if sub is not found. The search is done within the optional start and end indices.
print(x.find("xyz"))
# index(sub[, start[, end]]): This function is similar to find(), but it raises a ValueError if sub is not found in the string instead of returning -1.
print(x.index("xyz"))







