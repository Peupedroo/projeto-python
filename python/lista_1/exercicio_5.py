gerente= 8500
analista= 5000
suporte= 3000

aumento= gerente*12/100
novosalariog= aumento + gerente 

aumentoA= analista *15/100
novosalarioA= analista + aumentoA

suporteA= suporte * 15/100
suporteAG= suporte + suporteA


print (f"""
       o novo salario do gerente e. r$ {novosalariog}  
       o novo salario do analista .r$ {novosalarioA} 
       o novo salario do suporte.   r${suporteAG}""")