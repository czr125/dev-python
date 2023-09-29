def somar(val_soma1, val_soma2):
    resultado_soma = val_soma1 + val_soma2
    print(f'O resultado da soma é de: {resultado_soma}')

def multi(val_multi1, val_multi2):
    resultado_multi = val_multi1 * val_multi2
    print(f'O resultado da multiplicação é de: {resultado_multi}')

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1