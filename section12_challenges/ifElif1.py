# Calculo de IMC - Índice de Massa Corporal

'''
Qual é a sua altura em cm: 
Qual é o seu peso em kg:
'''

# MENOR QUE 18,5 = MAGREZA
# ENTRE 18,5 e 24,9 = NORMAL
# ENTRE 25,0 e 29,9 = SOBREPESO
# ENTRE 30,0 e 39,9 = OBESIDADE
# MAIOR QUE 40,0 = OBESIDADE GRAVE

altura = float(input('Qual a sua altura em cm? '))
peso = float(input('Qual o seu peso em KG? '))
imc = peso / (altura/100)**2

def calc_imc():
    if imc < 18.5:
        print(f'Seu IMC é de: {imc} e seu estado é de MAGREZA')
    elif imc >= 18.5 and imc < 24.9:
        print(f'Seu IMC é de: {imc} e seu estado é de NORMAL')
    elif imc >= 25.0 and imc < 29.9:
        print(f'Seu IMC é de: {imc} e seu estado é de SOBREPESO')
    elif imc >= 30.0 and imc < 39.9:
        print(f'Seu IMC é de: {imc} e seu estado é de OBESIDADE')
    else:
        print(f'Seu IMC é de: {imc} e seu estado é de OBESIDADE GRAVE')

calc_imc()