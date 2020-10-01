print("This program  print make a list for a range that is take input from user ")
l=int(input("L : ")) #initial range
e=int(input("E : ")) #Final range
li=[]
try:
   for j in range(l,e+1):
       li.append(j)
except:
       print("please Put value sequence wise as L<E")
print(li)
