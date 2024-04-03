valores=[]


for i in range (1,21):
    num = int(input("Digite o número {}: "))
    valores.append(num)
if valores:
    maior= menor = valores[0]

for valor in valores[1:]:
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor



print("esse e seu valor mais alto",maior)
print("esse e seu valor mais baixo ",menor)