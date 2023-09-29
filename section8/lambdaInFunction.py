# Lambda function
    # É uma função (pequena) sem nome
    # Pode ter varios argumentos mas somente uma expressão
    # Muito utilizado dentro de outras funções
    # Código mais limpo

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))

