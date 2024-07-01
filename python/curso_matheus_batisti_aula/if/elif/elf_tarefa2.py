renda = float (input("qual a sua renda "))
limite = 0
if renda < 2000:
    limite = 1000
elif renda < 4000:
    limite = 2000
elif renda < 10000:
    limite = 3000
elif renda > 10000:
    print ("vc precisa falar com o nosso gerente")
    limite = 3000


print (f"paramens seu limitefoi de {limite}")