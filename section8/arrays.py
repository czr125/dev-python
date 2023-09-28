from array import array # Precisa ser importada -> Module

# Array(Matriz)
    # Similar a listas
    # Melhor performance

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd']) # -> 'u' é codigo para wchar (string)
numeros_i = array('i', [10, 20, 30, 40]) # -> 'i' é codigo para integer (int)
numeros_f = array('f', [1.2, 2.2, 3.2]) # -> 'f' é codigo para float (float)
 
print(letras)
print(numeros_i)
print(numeros_f)
