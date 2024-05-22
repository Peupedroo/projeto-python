produtos = {}

def adicionar_produtos (codigo, nome, quantidade, preco):
    produtos[codigo] = {
        "codigo":codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco 
    }

def remover_produto (codigo):
    if codigo in produtos:
        del produtos[codigo]
    else:
       print ("esse codigo nao existe no banco de dados")
    
def atualizar_produto (codigo, nome=None, quantidade=None, preco=None):
    if codigo in produtos:
        produto = produtos[codigo]
        if nome :
                produto["nome"] = nome 
        elif quantidade:
                produto["quantidade"] = quantidade
        elif preco:
                produto["preco"] = preco
    else:
        print ("esse codigo nao existe no banco de dados")

def listar_produtos ():
    if produtos :
        for codigo, produto in produtos.items():
            print (f"o codigo do produto e :{codigo}, nome: {produto["nome"]}, quantidade : {produto["quantidade"]}, preço : {produto["preco"]} ")
    else :
         print ("esse codigo nao existe")
        
adicionar_produtos("001", "camiseta", 50, 29.99)
listar_produtos()
#da