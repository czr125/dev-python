# Desafio com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna
o ponto de cozimento em português. O usuário deverá fornecer a temperatura.

Temperatura - Cozimento
120ºF ou 48º - Rare(Selada)
130ºF ou 54º - Medium rare (Ao ponto para o mal passado)
140ºF ou 60º - Medium (ao ponto)
150ºF ou 65º - Medium well (Ao ponto para o bem passado)
160ºF ou 71º - Well done (Bem passada)
'''

def ponto_carne():
    temperatura = int(input('Insira a temperatura da carne: '))
    if temperatura <= 48:
        print(f'O ponto da carne é selada')
    elif temperatura in range(48, 53):
        print(f'O ponto da carne é ao ponto para o mal passado')
    elif temperatura in range(54, 59):
        print(f'O ponto da carne é ao ponto')
    elif temperatura in range(60, 64):
        print(f'O ponto da carne é ao ponto para o bem passado')
    elif temperatura in range(65,70):
        print(f'O ponto da carne é bem passada')
    else:
        print(f'A carne queimou')
    
ponto_carne()
