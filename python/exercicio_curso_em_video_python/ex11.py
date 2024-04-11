larg= float (input("qual e a largura da sua parede: "))
altura= float (input("qual e a altura da sua parede: "))
area= larg*altura 
tinta= area /2
print ("sua parede tem dimencao de {}x{} e a sua area e de {} m2.".format (larg,altura, area))
print("e para pintar essa parede vc precisa de {} l".format(tinta))