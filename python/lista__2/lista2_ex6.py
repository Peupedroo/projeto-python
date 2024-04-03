while True:
    numero = int(input("Digite um número de 0 a 10: "))
    
    if 0 <= numero <= 10:
        multi = range(10+1)
        for i in multi:
            print(numero * i)
        break
    else:
        print("Esse valor é inválido. Por favor, digite um número de 0 a 10.")

