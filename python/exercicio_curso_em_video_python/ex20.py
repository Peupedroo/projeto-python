import random
nome=[]

for i in range (1,5):
    nomes =str (input(f"digite o {i} nomes : "))
    nome.append(f"{i}: {nomes}s")
    

random.shuffle(nome)
print("a ordem e   ")
print (nome)