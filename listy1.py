# L = [3,7,6,1,3,3,5,4]
# print(L)
# print(L[1])
# print(L[6])
# print(len(L))

# for elem in L:
#     print(elem, end=" ")
# print("\n")

from random import randint
L = [randint(1,21) for i in range(20)]
print(L)
print(max(L))
print(min(L))
print(L.count(max(L)))