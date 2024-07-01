# Dicionário para armazenar os cadastros dos produtos
cadastro_produtos = {}

# Função para cadastrar um novo produto
def cadastrar_produto(codigo, nome, preco):
    cadastro_produtos[codigo] = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco
    }

# Função para remover um produto pelo código
def remover_produto(codigo):
    if codigo in cadastro_produtos:
        del cadastro_produtos[codigo]
    else:
        print(f"Produto com código {codigo} não encontrado.")

# Função para atualizar o cadastro de um produto
def atualizar_produto(codigo, nome=None, preco=None):
    if codigo in cadastro_produtos:
        produto = cadastro_produtos[codigo]
        if nome:
            produto["nome"] = nome
        if preco:
            produto["preco"] = preco
    else:
        print(f"Produto com código {codigo} não encontrado.")

# Função para listar todos os produtos cadastrados
def listar_produtos():
    if cadastro_produtos:
        for codigo, produto in cadastro_produtos.items():
            print(f"Código: {codigo}, Nome: {produto['nome']}, Preço: {produto['preco']}")
    else:
        print("Nenhum produto cadastrado.")



print("\nCadastro de Produtos")
cadastrar_produto(101, "Caneta", 1.50)
cadastrar_produto(102, "Caderno", 10.00)
listar_produtos()
atualizar_produto(101, preco=1.75)
remover_produto(102)
listar_produtos()