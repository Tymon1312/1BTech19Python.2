
a = int(input())
b = int(input())
c = int(input())
d = int(input())
x, y = b, d
ilocz = x * y 
while y>0:
    x, y = y, x%y
NWW = ilocz//x
e = (NWW// b)*a
g = (NWW//d)*c
h = e+g
print(f"{a}/{b} + {c}/{d} = {e}/{NWW} +{g}/{NWW} = {h}/{NWW} ")