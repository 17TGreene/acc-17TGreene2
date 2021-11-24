list0 = []
print(list0)
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list1[19] = "21"
print(list1[19])
print(list1[-1])
print(list1[0:6])
print(list1[6:])
del list1[19]
list1.append(21)
list1.extend([22,23,24])
list1.insert(19,20)
print(list1)
list1.remove(24)
print(list1.pop(22))
print(list1.index(21))
print(list1.count(1))
list1.reverse()
print(list1.copy())
list1.clear()
