import seaborn as sns
import matplotlib.pyplot as plt

arquivo = open("../../Documents/Processo Seletivo Estágio/CrashData.csv", "r")

linhas_separadas = []

for linha in arquivo.readlines():
    colunas = linha.split(',')
    linhas_separadas.append(colunas)

arquivo.close()

soma_mulher = 0
qtd_mulher = 0
soma_homem = 0
qtd_homem = 0

for linha in linhas_separadas:
    if linha[3] == '2021':
        if linha[12] == 'Male':
            soma_homem += int(linha[13])
            qtd_homem += 1
        elif linha[12] == 'Female':
            soma_mulher += int(linha[13])
            qtd_mulher += 1

media_homem = soma_homem / qtd_homem
media_homem_format = round(media_homem,2)
media_mulher = soma_mulher / qtd_mulher
media_mulher_format = round(media_mulher,2)
print('No ano de 2021, a média de idade dos homens que morreram em acidentes de trânsito na Austrália foi de ',media_homem_format)
print('No ano de 2021, a média de idade das mulheres que morreram em acidentes de trânsito na Austrália foi de ',media_mulher_format)
x = ['Homem','Mulher']
y = [media_homem_format,media_mulher_format]

sns.barplot(x=x, y=y)
plt.title('Média da idade de morte no transito em 2021 na Austrália')
plt.show()