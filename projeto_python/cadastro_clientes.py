# Dicionário para armazenar os cadastros dos clientes
cadastro_clientes = {}

# Função para cadastrar um novo cliente
def cadastrar_cliente(codigo, nome, idade):
    cadastro_clientes[codigo] = {
        "codigo": codigo,
        "nome": nome,
        "idade": idade
    }

# Função para remover um cliente pelo código
def remover_cliente(codigo):
    if codigo in cadastro_clientes:
        del cadastro_clientes[codigo]
    else:
        print(f"Cliente com código {codigo} não encontrado.")

# Função para atualizar o cadastro de um cliente
def atualizar_cadastro(codigo, nome=None, idade=None):
    if codigo in cadastro_clientes:
        cliente = cadastro_clientes[codigo]
        if nome:
            cliente["nome"] = nome
        if idade:
            cliente["idade"] = idade
    else:
        print(f"Cliente com código {codigo} não encontrado.")

# Função para listar todos os clientes cadastrados
def listar_clientes():
    if cadastro_clientes:
        for codigo, cliente in cadastro_clientes.items():
            print(f"Código: {codigo}, Nome: {cliente['nome']}, Idade: {cliente['idade']}")
    else:
        print("Nenhum cliente cadastrado.")

# Exemplo de uso das funções
cadastrar_cliente(1, "João", 30)
cadastrar_cliente(2, "Maria", 25)
listar_clientes()
atualizar_cadastro(1, idade=31)
remover_cliente(2)
listar_clientes()
