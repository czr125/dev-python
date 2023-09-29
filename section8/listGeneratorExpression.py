from sys import getsizeof # Verifica a quantidade de memoria alocada 

# Generator Expressions
    # Uma forma mais rápida para listas, dicionários e etc
    # Menos memória alocada
    # Valores em bytes

numero = [x * 10 for x in range(1000000)]
print(type(numero))
print(getsizeof(numero))

print('====================')

numero = (x * 10 for x in range(1000000)) # Forma muuuito mais leve de utilizar 
print(type(numero))
print(getsizeof(numero))