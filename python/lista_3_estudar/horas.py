def calculadora(hora):
    if hora > 40:
        hora_extra = hora - 40
        pagamento = (40 * 33.30) + ((hora_extra * 33.30) * 1.25)
    else:
        pagamento = hora * 33.3
    return pagamento

print(calculadora(41))