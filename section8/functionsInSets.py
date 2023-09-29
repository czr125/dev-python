list1 = set([1, 2, 3, 4, 5, 6]) # Lista que foi tornada em set
s1 = {1, 2, 3, 4, 5, 6} # Set feito com chaves

s1.add(7)
s1.update([7, 8, 9, 10]) # Gera erro se não tiver o item desejado na lista
s1.remove(10) # Não gera erro mesmo que não tenha o item na lista

print(s1)