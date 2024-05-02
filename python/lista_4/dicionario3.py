pacientes={
    1001 : {"nome": "pedro","idade": 19,"telefone": "4799203003" },
    1002 : {"nome": "jagunco","idade": 10012,"telefone": "8992883928"},
    1003 : {"nome": "exroai","idade": 100121, "telefone": "92002293"},
    1004 : {"nome": "carlos daniel","idade":123, "telefonr": "9922123"}
    
}

medicos= {
    "m001" : {"nome": "macedo", "idade ": 41, "telefone": "83900990909", "especialista em ": "urologia"},
    "m002" : {"nome": "macedo", "idade": 41, "telefone": "839009309409", "especialista em ": "neurologista"},
    "m003" : {"nome": "macedo", "idade": 89 , "telefone": "83998899889","especialista em": "estomatologia" }
}

agenda={
    "ag001" : {"paciente": 1001,"medico": "m003", "data": "12/05/2024", "hora" : "16:24" },
    "ag002" : {"paciente": 1004,"medico": "m002", "data": "12/05/2024", "hora" : "17:50" },
    "ag003" : {"paciente": 1003,"medico": "m001", "data": "12/05/2024", "hora" : "18:24" }

}

for i, j in pacientes,medicos,agenda.items():
    print(f"{i}, {j}")