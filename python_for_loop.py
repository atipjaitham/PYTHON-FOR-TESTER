# for loop

cities = [('Thailand', 'Bangkok'), ('China', 'Beijing'), ('Japan', 'Tokyo'), ('Korea', 'Soul')]
citiex = {'Thailand','Beijing'}
# for country,city in cities:
#     print("country is "+country+" and city is "+city)
my_dictionary = dict(cities)
print(my_dictionary)
for country,city in my_dictionary.items():
     print(country,city)
     for s in country:
        print(s)