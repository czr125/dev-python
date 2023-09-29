# Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, boolean...

#         Key   |  Value
aluno = {'nome': 'Cezar', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

# aluno['nome'] = 'Jose'
# aluno.update({'nome': 'Josias', 'nota_final': 'B'})
# aluno.update({'endereco': 'rua A'}) # Adiciona campos no dicionario

del aluno['idade']

print(aluno)


print(aluno.get('endereco', 'Não existe esse campo')) # get é uma forma de evitar erros no codigo caso o campo não exista
