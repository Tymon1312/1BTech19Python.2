# n = int(input())
# for i in range(n):
#   print("*-")

# #sposob 2
# n = int(input())
# print("*-")*n

#zad 2
# n = int(input())
# for i in range(1,n+1):
#    print("*"*i, end="")
#    if i % 2 == 0:
#       print("--", end="")
#    else:
#       print("||", end="")
#zad 3
# n = int(input())
# for i in range(1,n+1):
#     print("*", end="")
#     if i % 2 == 0:
#        print("-"*i, end="")
#     else:
#        print("||"*i, end="")
#zad 7
n = int(input())

for i in range(n):
    for j in range(n):
        print(f"({i},{j})", end="")