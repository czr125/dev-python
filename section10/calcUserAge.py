from datetime import datetime

# Criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    def nome_completo(self):
        return f'O nome completo do usuário é: {self.nome} {self.sobrenome}'
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return f'A idade do usuário é de: {self.ano_nascimento} anos. '

# Criar o objeto
usuario1 = Funcionarios('Cezar', 'Mutran', 2004)
usuario2 = Funcionarios('Carol', 'Silva', 2002)

# Print
print(Funcionarios.idade_funcionario(usuario1))