def calimc(peso, altura):
    return peso / (altura ** 2)

def compo_usu(imc):
    if imc < 18.5:
        return "Você está abaixo do peso."
    elif 18.5 <= imc <= 25:
        return "Peso ideal."
    else:
        return "Você está obeso."

def informacoes_usuario(nome, idade, peso, altura, sexo):
    contar_idade = len(nome)
    if idade < 18:
        maioridade = "Você é adulto."
    else:
        maioridade = "Você é bebê."
    
    imc = calimc(peso, altura)
    composicao = compo_usu(imc)

    return contar_idade, maioridade, imc, composicao

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual sua altura? "))
sexo = input("Qual seu sexo? ")

resultado = informacoes_usuario(nome, idade, peso, altura, sexo)

print(f"O nome {nome} possui {resultado[0]} caracteres.")
print(f"{resultado[1]}")
print(f"Seu IMC é {resultado[2]:.2f}.")
print(f"{resultado[3]}")