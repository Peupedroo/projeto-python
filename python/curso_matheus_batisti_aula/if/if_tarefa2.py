primeiro = int(input("escreva um numero"))
segundo = int(input("escreva outro numero"))

if primeiro > segundo :
    print (f"o numero {primeiro} e maior que o numero {segundo}")
elif primeiro == segundo:
    print (f"os numeros sao iguais tanto {primeiro} quanto {segundo}")
else:
    print(f"o numero {segundo} e maior que o numero {primeiro}")