valor = int(input('Insira o valor do produto: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f"O valor final do seu produto será de R${valor}")
    break
