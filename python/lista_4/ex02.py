
numero=[]

while True:
    
    um_numero=input("digite um numero ou digite parar parar encerrar ")
    if um_numero.lower()=="parar":
        break
    elif not um_numero.isdigit():
        print("digite um numero valido ")
    else :
        numero.append(int(um_numero))
if numero:
    soma = sum(numero)
    print("A soma dos números é: {}".format(soma))
else:
    print("Nenhum número foi inserido.")