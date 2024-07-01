numero = False
while numero == False:
    perg = int (input("escolha um numero para aparecer na tela"))
    if perg > 0 :
        print (perg)
    else:
        print ("vc parou o loop")
        break
    