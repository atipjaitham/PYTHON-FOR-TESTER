demo_dict2 = {"qa":"testurl", "uat":"uaturl", "preprod":"preprodurl"}
# get()
print(demo_dict2.get("preprod")) # preprodurl
# keys()
print(demo_dict2.keys()) # dict_keys(['qa', 'uat', 'preprod'])
# items()
print(demo_dict2.items()) # dict_items([('qa', 'testurl'), ('uat', 'uaturl'), ('preprod', 'preprodurl')])
# values()
print(demo_dict2.values()) # dict_values(['testurl', 'uaturl', 'preprodurl'])
# pop()
print(demo_dict2.pop("uat"))
# popitem()
print(demo_dict2.popitem())
# update()
print(demo_dict2.update({"preprod":"preprodurl"}))
# copy()
demo_copy = demo_dict2.copy()
# clear()
demo_copy.clear()
print(demo_dict2)
print(demo_copy)



