arquivo = open('numeros.csv','r')
listagem = arquivo.read()
arquivo.close()

lista = listagem.split(',')
soma = 0

for num in lista:
    num = int(num)
    if num % 2 == 1:
        soma += num

print(soma)