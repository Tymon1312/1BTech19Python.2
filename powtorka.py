#potęgowanie np. 2**3
print (11/4)
print (11%4)
#ostatnie 2 cyfry
n = 12356
print(n%100)
#cyfra setek
n = 12345
print ((n%10000)//1000)
# pierwiastek
from math import sqrt
print (sqrt(576))
print (576**(1/2))
print (8**(1/3))
#operatory porównawcze == >= <= > < !=
#pętla z liczbami 3-cyfrowymi podzielnymi przez 13 i niepodzielnymi przez 4
for i in range(100,1000):
   if i %13 == 0 and i % 4 != 0:
     print(i, end=" ")
#łączenie warunków
a, b, c = 3 , 5 , 7
if a < b < c:
   print("Eppure si move")
n = 24
suma = 0
for i in range(1,25):
   if n % i == 0:
       print(i)
       suma = suma + i
print("suma", suma)


#suma początkowcyh liczb 3 cyforwych

k = 4
suma = 0
ilosc = 0
for i in range(100,1000):
    suma = suma + i 
    ilosc = ilosc + 1
    if ilosc == k:
        break
print(suma)

k = 4
suma = 0
for i in range(100,100+k):
    suma = suma + i 
print(suma)
      