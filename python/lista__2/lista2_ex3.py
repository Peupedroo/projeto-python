def menu ():
    print ("-- MENU ----")
    print (" {1 } continuar     .")
    print()
    print(" {2 } sair .    ")

while True:
    menu()
    escolha = input ("qual sua oppçao :   ")
      
    if escolha=="1":
         print ("vc escolheu contuinuar:     ")
    elif  escolha == "2":
        print ("VOCE SAIU .  ")
        break 
    else :
        print ("NENHUMA ESCOLHA VALIDA TENTE NOIVAMENTE .   ")
