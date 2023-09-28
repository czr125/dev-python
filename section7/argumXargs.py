# Varios argumentos (xargs)
# Criar uma função que some varios numeros

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2,10,20,4,20)

print(x)