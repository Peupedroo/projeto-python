numero = int (input("digite um numero"))

if numero < 10:
    print ("o nuemro tem que ser maior que 10")
else :
    if numero < 20:
        print ("o numero e menor que 20")
        print (numero * 2)
    else :
        print ("o numero e maior que 20")
        print(numero * 5)