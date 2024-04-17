marcas=["GM","FIAT","VOLKSWAGEN","FORD","HONDA","TOYOTA","GURGEL" , "DODGE"]

marcas.insert(3,"hyundai")
marcas.insert(4,"BMW")
marcas.insert(5,"nissan")

marcas[marcas.index("GM")]= "CHEVROLET"

marcas.sort()

print("esse foi o nome das marcas ")

for marca in marcas :
    print(marca)