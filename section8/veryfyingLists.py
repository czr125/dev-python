
cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('Temos a cor no estoque')
else:
    print('Não temos essa cor em estoque')