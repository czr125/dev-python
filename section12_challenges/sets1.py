# Desafio com 'sets'

'''

Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = funcionarios que tem carro e trabalham a noite
Lista2 = funcionarios que tem carro e trabalham durante o dia
Lista3 = funcionario que não tem carro

'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

tem_carro_noite = set(tem_carro).intersection(turno_noite)
tem_carro_dia = set(tem_carro).difference(turno_noite)
nao_tem_carro = set(funcionarios).difference(tem_carro)

print(tem_carro_noite)
print(tem_carro_dia)
print(nao_tem_carro)
