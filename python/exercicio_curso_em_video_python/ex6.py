

num= int(input("quantas provas vc fez "))
disc= str(input("qual a materoa que vc quer a media   "))
if num<=0:
      print("digite um numero correto")
else:
    tentativas=0

for i in range (num):
     if num<=0:
      print("digite um numero correto")
     
     
     notas =int (input("digite suas nota {}  ".format (i+1)))
     tentativas+=notas
     
     
     
media =(tentativas)/num

print ("vc tirou na {} a nota de {}" . format (disc, media))

