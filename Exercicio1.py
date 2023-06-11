import random

lista_aleatoria = []
for i in range(0,20):
    num_aleatorio = random.randint(1,100)
    lista_aleatoria.append(num_aleatorio)

maior_valor = max(lista_aleatoria)

print(lista_aleatoria)
print('O maior número da lista criada é %d.'%(maior_valor))