# list
# lst = []
# lst1 = list()
# lst.append(2)
# lst.append(3)
# print(lst)

list1 = [1, 2, 3, 6, 78, 77 ,189]
# list2 = list1 # shallow copy

# ver 1
# list2 = []

# for number in list1:
#     list2.append(number)

# #ver 2
# list2 = list1.copy()

# ver 3
# import copy
# list2 = copy.deepcopy(list1)

# ver 4
list2 = list1[:]
list2[0] = 25

print(list1)
print(list2)

# print(list1[1:3])
# print(list1[1:6:2])
# print(list1[:3])
# print(list1[3:])
# print(list1[:])
# print(list1[::-1])
# print(list1[-1])
# print(list1[len(list1) - 1])

print("list1".find('a'))