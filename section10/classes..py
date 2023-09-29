# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uuma Class (instancias)
    # Classes são utlizadas para agrupar dados e funções, podendo reutilizar
    # ===========
    # Class: Frutas
    # Objects: Abacate, Banana, Maçã, Uva...

class Funcionarios:
    nome = 'Helena'
    sobrenome = 'Sousa'
    data_nascimento = '12/01/2003'


usuario1 = Funcionarios()

print(usuario1.nome, usuario1.sobrenome, usuario1.data_nascimento)