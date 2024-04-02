idade25=0
idade26=0
idade69=0
opcao=0
while True:
    np= input ("escreva a idade da pessoa, ")
    print ("caso tenha terminado de escrever , digite 2")
    
    if np  == 2:
     print ("vc parou ")
     break
idade= int (np)

if 0<=idade<= 25:
       idade25 +=1
elif 2<= idade <= 60:
        idade26+=1
else :
       idade69+=1
       opcao= input("digite s,n ")
print ("quantidade de pessoas por idade")
print ("0 a 25 anos ",idade25 )
print ("quantidades de pessoas de 0 a 26",idade26)
print ("quantidades de pessoas de 60 pra cima ",idade69)      

