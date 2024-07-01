numeros = []
perg = int(input("digite um numero"))
while True :
    if perg >=10:
        soma_digitos = sum(int(digito) for digito in str(perg))
        numeros.append(soma_digitos)
        break
    else :
        print("esse numero nao e valido")
        
    
print (F"esses sao as somas dos numeros {numeros}")