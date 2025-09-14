my_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list1 = []
new_list2 = []
sett = set()
for i in my_list:
    new_list1.append(i + 2)
    if i > 5:
        new_list2.append(i + 2)

for i in new_list1:
    if i in new_list2:
        sett.add(i)

print(my_list)
print(sett)

