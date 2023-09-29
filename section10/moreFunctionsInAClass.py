# Criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
    def nome_completo(self):
        return f'O nome completo do usuário é: {self.nome} {self.sobrenome}'
    
    def data_nasc(self):
        return f'A data de nascimento do usuário é: {self.data_nascimento}'

# Criar o objeto
usuario1 = Funcionarios('Cezar', 'Mutran', '07/06/2004')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2002')

# Print
print(usuario1.nome + ' ' + usuario1.sobrenome)
print(usuario2.nome + ' ' + usuario2.sobrenome)
print(usuario1.nome_completo())
print(usuario1.data_nasc())
# print(type(usuario1.nome_completo()))
print(Funcionarios.nome_completo(usuario1))