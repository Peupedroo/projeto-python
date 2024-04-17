import funcoes_ex1

produto=(input("qual o nome do seu produto "))
peso_em_gramas= int(input("digite o valor do seu peso em gramas "))
valor_em_dolar = float(input("qual o valor do produto em dolar "))

valor_em_reais=funcoes_ex1.converter_dolar_real(valor_em_dolar)
valor_do_frete=funcoes_ex1.valor_frete(peso_em_gramas)

print(f"/nproduto:{produto}")
print("valor em reais {}".format(valor_em_reais))
print("o valor do frete {}".format(valor_do_frete))