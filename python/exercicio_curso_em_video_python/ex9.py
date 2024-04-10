
numero= int(input("digite um numero:" ))
while True:
    
    if 0<= numero :
    
        for i in range (1,11):
           mult = (numero * i)
       
           print ("{} x {} = {}".format(numero,i,mult))
        break