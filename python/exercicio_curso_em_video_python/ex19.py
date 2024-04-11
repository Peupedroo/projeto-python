import random
nomes=[]
for _ in range(9):
 nome=(str(input ("escolha um nome ")))
 nomes.append(nome)


escolha=random.choice(nomes)
print ("o nome escolhido foi {}".format (escolha))