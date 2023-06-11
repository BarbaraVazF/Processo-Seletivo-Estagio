paravra = input('Digite uma palavra: ')
lista = []

for letra in paravra:
    lista.append(letra)

tamanho_palavra = len(lista)
eh_palindromo = True

for pos in range(0, tamanho_palavra//2):
    if lista[pos] != lista[-(pos+1)]:
        eh_palindromo = False

if eh_palindromo == True:
    print('Sim, a palavra %s é palíndroma'%(paravra))
else:
    print('Não, a palavra %s não é palíndroma'%(paravra))
