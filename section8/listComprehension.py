# List Comprehension
    # Mais simples de se escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressão for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

# frutas2 = []

# for item in frutas1:
#     if 'b' in item:
#         frutas2.append(item)

frutas2 = [iten for iten in frutas1 if 'b' in iten] # Forma mais simples e rapida de juntar itens em uma lista vazia


print(frutas2)