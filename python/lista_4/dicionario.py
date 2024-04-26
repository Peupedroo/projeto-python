masulino={}
feminino={}

while True:
    sexo=input("qual o seu sexo (m ou f) se quiser parar use o 0 ")
    
    if sexo == "m":
        idadem= int (input("qual sua idade  "))
        nome= str(input("qual seu nome"))
        masulino[nome]=idadem 
    
    
    elif sexo == "f":
        idadef = int(input("qual sua idade:  "))
        nomef=str(input("qual seu nome:  "))
        feminino[nomef]=idadef
    
    
    elif sexo== "0":
        break
    
    
    else:
        print("valor invalido")  
    
print("o dicionario masculino ficou ", masulino)
print("o dicionario feminino ficou ", feminino)