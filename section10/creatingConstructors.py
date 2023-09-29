# Criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

# Criar o objeto
usuario1 = Funcionarios('Cezar', 'Mutran', '07/06/2004')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2002')

# Print
print(usuario1.nome, usuario1.sobrenome)
print(usuario2.nome, usuario2.sobrenome)

# Criar os parametros do usuario1

# usuario1.nome = 'Elena'
# usuario1.sobrenome = 'Cabral'
# usuario1.data_nascimento = '12/01/2003'

# # Criar os parametros do usuario2

# usuario2.nome = 'Carol'
# usuario2.sobrenome = 'Silva'
# usuario2.data_nascimento = '22/03/2005'
