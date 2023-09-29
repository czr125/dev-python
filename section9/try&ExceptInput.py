try:
    valor = int(input('Insira o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor, insira um número válido')

print('Mais codigo')