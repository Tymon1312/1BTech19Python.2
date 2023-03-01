T = [50,20,10,5,2,1]
T.sort(reverse=True)
x = int(input("Reszta: "))
for i in T:
    ilosc = x// i
    if ilosc > 0:
        x = x - ilosc * i
        print(f"{ilosc} razy {i}")

  #druga wersja
T = [50,20,10,5,2,1]
T.sort(reverse=True)
W = []
x = int(input("Reszta: "))
for i in T:
    ilosc = x//i
    if ilosc > 0:
        x = x - ilosc * i
        for j in range(ilosc):
            W.append(i)
print(W)
                  