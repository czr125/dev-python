produtos = ['arroz', 'feijao', 'laranja', 'banana', 4, 5, 6]

item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]

item1, item2, item3, item4, *outros = produtos

print(item1, item4)
print(produtos)
print(outros)