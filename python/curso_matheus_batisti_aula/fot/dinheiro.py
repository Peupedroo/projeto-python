dinheiro = int (input("quanto dinheiro vc quer  "))


notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0

while dinheiro > 0:
    while dinheiro >= 100:
        notas_100 +=1
        dinheiro -=100
    while dinheiro >= 50:
        notas_50 +=1
        dinheiro -=50
    while dinheiro >= 20:
        notas_20 +=1
        dinheiro -=20
    while dinheiro >= 10:
        notas_10+=1
        dinheiro-=10
    while dinheiro >= 1:
        notas_1 += 1
        dinheiro -= 1

print (f"voce sacou {notas_100} em nota de 100$, e {notas_50} nota de 50$, e {notas_20} de 20$, e notas {notas_10} de 10$, e {notas_1} nota de 1$",)
     
     