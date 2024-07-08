#solicita o numero para o usuario
numero = int (input("digite um numero  "))

#faz a contagem das divisoes 
divisoes = 0

#inicializa o contador apartir do numero fornecido
contador = numero

#inicializa o loop
while contador > 0:
    
    if numero % contador == 0:
        divisoes += 1

    contador -= 1




if divisoes == 2:
    print (f"o {numero} e primo")
else:
    print (f"o {numero} nao e primo")
