# Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, boolean...

#         Key   |  Value
aluno = {
    'nome': 'Cezar', 
    'idade': 16, 
    'nota_final': 'A', 
    'aprovacao': True, 
    'materias': ['Fisica','Matematica', 'Ingles']
}


# print(aluno)
# print(aluno.get('materias'))
# print(len(aluno))
print(aluno.items())
print(aluno.keys())
print(aluno.values())