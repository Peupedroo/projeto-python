alfabeto=["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","U","V","Y","X"]

def valor_para_letra (numero):
    if 1<=numero<=26:
        return alfabeto[numero-1]
    else:
        return "numero fora do intervalo dado" 


def valor_impar_par(numero):
    if numero %2==0:
        return "o valor e par "
    else:
      return "o numero e impar "
    


numero=int(input("digite um numero para que eu fale qual letra ele representa:  "))


resultado = valor_para_letra(numero)


letra = valor_para_letra(numero)
par_impar = valor_impar_par(numero)

print(f"A letra que corresponde ao número {numero} é {letra} e é {par_impar}.")