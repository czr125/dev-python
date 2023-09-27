linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas): # Roda 6 vezes o loop de fora - Primeiro 1 contendo 6 de dentro
    for c in range(colunas): # Roda 6 vezes o loop de dentro 
        print(simbolo, end="")
    print()