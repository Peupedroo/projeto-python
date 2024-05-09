def nome (usuario):
    print (len(usuario))
    return


def ano (idade):
    ano_nascimento =  2024 - idade
    print (idade)
    return ano_nascimento

ida = int (input("qual sua idade: "))
nomeusu = str (input("qual o seu nome"))
numero_letras = nome(nomeusu)
data_nasciemnto_ = ano(ida)

print (data_nasciemnto_)
print (numero_letras)