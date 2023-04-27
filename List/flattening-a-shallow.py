
list = [[1,2,3],[3,4,5],[6,7,8]]

list_1 = []

for x in list:
    for y in x:
        list_1.append(y)

print(list_1)


# this below code is to remove the repeated element
list_2 = set(list_1)
print(list_2)

