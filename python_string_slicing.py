# s[i:j] - slice of s from i to j
# s[i:j:k] - slice of s from i to j with step K
# s[stratindex:endindex:step]

s = "welcome to software testing mentor anf rcv academy"
y = "name, age, city"
print(s[-1])
print(s[4:8])
print(s[4:8:2])
print(s[0:])
print(s[:])
print(s[::-1])
print(y.index(','))
print(y[0:y.index(',')])