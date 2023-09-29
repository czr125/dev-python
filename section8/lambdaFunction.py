# Lambda function
    # É uma função (pequena) sem nome
    # Pode ter varios argumentos mas somente uma expressão
    # Muito utilizado dentro de outras funções
    # Código mais limpo

# def somar(x):
#     return x + 10

# print(somar(2))

somar = lambda x,y: x + y + 10
print(somar(10,20))