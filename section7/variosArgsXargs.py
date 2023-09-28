# Varios argumentos (xargs) identificando o Parametro

# Criar uma função que armazena numeros e strings (dados)

def agencia(**carro): # -> ** = Varios argumentos e varios parametros 
    return carro

print(agencia(marca='Gol', cor='Branco', motor=1.0, placa=1234))
print(agencia(marca='Classic', cor='Azul', motor=1.4, placa=1012))
print(agencia(marca='Gol', cor='Vermelho', motor=1.6))