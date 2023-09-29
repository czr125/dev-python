# Erros
    # Excelente para testes
    # Não realiza o 'stop' do programa
    # mensagens customizadas quando encontra um erro

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Erro de indice')
    