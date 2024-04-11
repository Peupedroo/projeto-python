#from math import sqrt
#oposto= float(input("qual o cateto oposto do seu triangulo "))
#adjacente=float(input("qual o cateto adjacente do seu triangulo "))
#hi= (oposto**2) +(adjacente**2)
#print ("o hipotenusa e {:.2f}".format (sqrt(hi)))
from math import hypot
co =float(input("digite seu cateto oposto "))
ca=float(input("digite seu cateto adjacente "))
hi= hypot(co,ca)
print("esse e o valor da hipotenusa {:.2f}" .format(hi))