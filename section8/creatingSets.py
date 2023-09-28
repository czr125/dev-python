# Set (listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1)
print(num1 | num2) # Union -> 
print(num1 - num2) # Diference ->
print(num1 ^ num2) # Synmetric Diference -> Tira os duplicados da lista
print(num1 & num2) # And -> O que é duplicado nas duas listas

print(len(num1))
# print(num1[0]) -> Não há index