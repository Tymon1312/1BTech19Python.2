#zad3
k = int(input())
l = int(input())
m = int(input())
if k==l and k!=m:
 print("k jest równe l")
else:
 if l==m and l!=k:
  print("l jest równe m")
 else:
  if k==m and k!=l:
   print("k jest równe m")
  else:
    print("nie ma takich samych")