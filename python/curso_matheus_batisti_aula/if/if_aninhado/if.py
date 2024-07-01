idade = int(input("qual sua idade"))

if idade >=18:
    print ("vc pode entrar na balada")

    metodo_pagamento = input("como vc vai pagar a entrada ")

    if metodo_pagamento == "dinheiro":
        print ("a fila do dinheiro e a numero 1")
    else:
        print("a fila de cartao e a numero 2")
else:
    print ("vc nao pode va pra casa")