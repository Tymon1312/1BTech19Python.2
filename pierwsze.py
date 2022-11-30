#sprawdzianie czy liczba jest pierwsza

# n = int(input())
# for i in range(2,n):
#   if n % i == 0:
#      print('Liczba nie jest pierwsza')
#      exit(0)
# print("liczba jest pierwsza")

#Generowanie liczb pierwszych

# n = int(input("Podaj do ilu mam szukać liczb pierwszych"))

# for i in range(2, n+1):
#     flaga = True;
#     for j in range(2, i):
#         if i % j == 0:
#            flaga = False
#            break
#     if flaga:
#        print(i, end=" ")


#drugi sposób
# n = int(input("Podaj do ilu mam szukać liczb pierwszych"))

# for i in range(2, n+1):
#     flaga = True;
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#            flaga = False
#            break
#     if flaga:
#        print(i, end=" ")
#3 generowanie liczb pierwszych (pierwsze n liczb pierwszych)
n =int(input())
i= 2
licznik= 0
while 1:
    flaga = True;
    for j in range(2,int(i**0.5)+1):
         if i % j == 0:
            flaga = False
            break
    if flaga == True:
     print(i, end=" ")
     licznik += 1
    if licznik == p:
         break
    else:
       i = i+1
      print(i, end=" ")