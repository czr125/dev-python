# Tuples
    # Armazenar mais de uma informação em variaveis
    # Manter a sequencia dos dados em uma variavel
    # Não podem ser alteradas(Immutable)
    # Lista de itens fixos que não podem ser alterados

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']

cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho') # Tupla é diferenciada pelos parenteses

print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_list * 2
duas_tuplas = cores_tuple * 2

print(duas_listas)
print(duas_tuplas)

cores_list.append('roxo')
print(cores_list)