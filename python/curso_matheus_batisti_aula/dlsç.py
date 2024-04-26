
soma=0
mult=1
sub=0

for _ in range(2):
    numero = int(input("Digite um número: "))
    soma += numero
    if sub == 0:  
        sub = numero
    else:
        sub -= numero
    mult *= numero

print(f"a soma e {soma}")
print (f"a subitracao e {sub}")
print (f"a mult e {mult}")