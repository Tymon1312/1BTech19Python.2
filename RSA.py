#PRE

# from math import gcd
# print(gcd(20,15))

# wybór dużych liczb peirwszych
p = 11
q = 13
print(p,q)

#obliczenie n=p*q i funkcji Eulera F=(p-1) * (q-1)
n = p * q
F = (p - 1) * (q - 1)
print(n)
print(F)

#generuj klucz publiczny e taki że, NWD(e,F)=1
from math import gcd
for i in range(2,F):
   if gcd(i,F) == 1:
      e = i 
      break
print(e,n)

#generujemy klucz prywatny d taki, że (d*e) %F = 1
for j in range(2,F):
    if ((j*e) % F) == 1:
        d = j
        break
print(d,n)

#przykład działania RSA
#m - moja wiadomość - message
#c = m**e % n (szyfrogram - cypher- wiadomość zaszyfrowana)
#t = c**d % n (tekst jawny czyli nasza wiadomość - text(message))

m = input()

for i in m:
   print((ord(i)**e)%n)