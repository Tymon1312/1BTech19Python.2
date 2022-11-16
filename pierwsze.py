#sprawdzianie czy liczba jest pierwsza

n = int(input())
for i in range(2,n):
  if n % i == 0:
     print('Liczba nie jest pierwsza')
     exit(0)
print("liczba jest pierwsza")