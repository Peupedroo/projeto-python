cadastro_clintes = {}

def cadastro (codigo, nome, idade ):
    cadastro_clintes [codigo] = {
        "codigo" :codigo,
        "nome"  :nome,
        "idade" :idade
    }

def remover_clientes (codigo):
    if codigo in cadastro_clintes:
        del cadastro_clintes [codigo]
                              

def atualizar_cadastro (codigo, nome= None, idade = None):
    if codigo in cadastro_clintes :
        codigos = cadastro_clintes[codigo]
        if nome:
            codigos["nome"] = nome
        elif idade :
            codigos ["idade"] = idade