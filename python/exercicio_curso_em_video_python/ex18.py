import math
numero= int(input("digite um angulo "))
seno=math.sin(math.radians(numero))
cosseno=math.cos(math.radians(numero))
tang=math.tan(math.radians(numero))

print( "o angulo {} tem o seno de {:.2f}".format (numero,(seno)))
print("o angulo {} tem o seu cosseno de {:.2f}".format (numero, cosseno))
print("o angulo {} tem a sua tangente {:.2f}". format(numero,tang))
