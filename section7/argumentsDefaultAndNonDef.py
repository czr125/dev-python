# Parametro --> Argumento
# Default = Aquele que você define o valor no parametro 
# Non=Default = Aquele que você não define o valor no parametro

def boas_vindas(nome=input('Insira seu nome: '),quantidade=input('Qual a quantidade do estoque? ')): # -> Parametro
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} notebooks')

boas_vindas() # -> Argumento