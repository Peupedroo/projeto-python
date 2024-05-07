pacientes={
    1001 : {"nome": "pedro","idade": 19,"telefone": "4799203003" },
    1002 : {"nome": "jagunco","idade": 10012,"telefone": "8992883928"},
    1003 : {"nome": "exroai","idade": 100121, "telefone": "92002293"},
    1004 : {"nome": "carlos daniel","idade":123, "telefone": "9922123"}
    
}

medicos= {
    "m001" : {"nome": "macedo", "idade": 41, "telefone": "83900990909", "especialista": "urologia"},
    "m002" : {"nome": "carlos", "idade": 41, "telefone": "839009309409", "especialista": "neurologista"},
    "m003" : {"nome": "alberto", "idade": 89 , "telefone": "83998899889","especialista": "estomatologia" }
}

agenda={
    "ag001" : {"paciente": 1001,"medico": "m003", "data": "12/05/2024", "hora" : "16:24", "especialista": "01" },
    "ag002" : {"paciente": 1004,"medico": "m002", "data": "12/05/2024", "hora" : "17:50", "especialista": "02"},
    "ag003" : {"paciente": 1003,"medico": "m001", "data": "12/05/2024", "hora" : "18:24", "especialista": "03"} 

}
print ("pacientes")


for paciente_id, paciente_info in pacientes.items():
     print(f"ID: {paciente_id} NOME: {paciente_info["nome"]} IDADE: {paciente_info["idade"]} TELEFONE: {paciente_info["telefone"]} MEDICO ")



 
for agenda_id, agenda_info in agenda.items():
    paciente_id = agenda_info.get ("paciente")
    paciente_info = pacientes.get(paciente_id)
    medico_id = agenda_info.get("medico") 
    medico_info = medicos.get (medico_id)
    
    especialidade_info = medico_info.get("especialista")
    
    print(f"ID: {agenda_id}, paciente: {paciente_info["nome"]} medico {medico_info ["nome"]}, especialista em : {especialidade_info} na data {agenda_info["data"]} e na hora {agenda_info["hora"]}")
    


