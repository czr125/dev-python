# Desafio com funções 

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deve fornecer as seguintes informações: Rendimento, altura e largura.

O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'
'''

rendimento = int(input('Quantos metros quadrados tem de rendimento a lata de tinta? '))
altura = int(input('Informe a altura da área que você deseja pintar: '))
largura = int(input('Informe a largura da área que você deseja pintar: '))

def calc_tinta():
    area = altura * largura
    latas_tinta = area / rendimento
    print(f'Com a area de {area}m2, você irá necessitar de {latas_tinta} latas de tinta. ')    

calc_tinta()
