lst = [25, 98, 78, 1 ,87, 332, 7]

for i in lst:
    i += 10
    # print(i, end=" ")

print(lst)


for i in range(len(lst)):
    lst[i] += 10

print(lst)