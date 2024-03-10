x = "This is a 'string' in double quotes"
y = 'This is a "string" in single quotes'
z = 'This is a \'string\' single quotes in single quotes'
z1 = "This is a \"string\" double quotes in double quotes"

zx = """
This is a
multiline string with 3 double quotes
"""
zy = '''
This is a
multiline string  with 3 single quotes
'''

print(x)
print(y)
print(z)
print(z1)
print(zx)
print(zy)

print("is" in zy) #chack words in variable result is boolean