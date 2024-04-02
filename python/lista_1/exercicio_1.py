
print("""
      {1}somar 
      {2}multiplicar
      {3}subtraçao
      {4}divisao""")
opçao=int (input( "qual sua opçao.    ")) 
n1= float(input("digite o primeiro numero.  "))
n2= float(input("digite o segundo numero.   "))


if (opçao==1):
    soma=n1+n2
    print("o resultado da soma e=  ",soma)

if(opçao==2):
    multiplicador=n1*n2
    print("o resultado da multiplicaçao.  ",multiplicador)

if(opçao==3):
    subtracao=n1-n2
    print("resultado da subtraçao.   ",subtracao)

if(opçao==4):
    div=n1/n2
    print("resultado da divsao.  ",div)







