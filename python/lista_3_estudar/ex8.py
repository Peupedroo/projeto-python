from random import randint
pc = randint (0,50)
print (" sou seu computador e estou sorteando um numero de 0 a 20 ")
print("sera que vc consegue acertar ")
tentativas=0

acerto=False
while not acerto:
    jogador =int ( input ("de seu palpite  ".format(tentativas+1)))
    tentativas+=1
    if jogador == pc:
        acerto=True
    else:
        if jogador< pc:
            print("tente um numero maior")
        else:
            print("tente um numero menor ")


print("acertou com {} tentativas ".format (tentativas))