

n = "1,3,7,9,2,20,5,69"
n1 = n.split(",")
# print(n1)
n1 = [int(x) for x in n1]
max_num = max(n1)
print(max_num)