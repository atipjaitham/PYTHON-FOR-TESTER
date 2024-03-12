list1 = ["Thailand", "China", "Japan", "Korea"]
list2 = ["Bangkok", "Beijing", "Tokyo", "Soul", "Taipei"]


total_cost = (45, 67, 65, 87)
sale_price = (55, 77, 89, 76)
# s = zip(list1,list2)
# print(list(s))

for x,y in zip(list1,list2):
    print(y,x)