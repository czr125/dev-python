def boas_vindas(nome):
    print(f'Olá {nome}') # -> Realizam uma tarefa

boas_vindas('Cezar')


def boas_vindas2(nome):
    return f'Olá {nome}' # -> Calcula e retorna um valor, armazena um valor no código

boas_vindas2('Augusto')

print(boas_vindas2('Augusto'))

x = boas_vindas('Cezar')
y = boas_vindas2('Augusto')

print(x)
print(y)