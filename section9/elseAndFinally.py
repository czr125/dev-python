try:
    valor = int(input('Insira o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor, insira um número válido')
finally:
    print('Codigo OK')

# else:
#     print('Usuário digitou um valor correto')
#     resultado = valor * 2
#     print(resultado)

print('Mais codigo')