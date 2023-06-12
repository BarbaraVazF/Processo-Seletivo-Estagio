import seaborn as sns
import matplotlib.pyplot as plt

arquivo = open("CrashData.csv", "r")

linhas_separadas = []

for linha in arquivo.readlines():
    colunas = linha.split(',')
    linhas_separadas.append(colunas)

arquivo.close()

primeiro_gp = '0_to_16'
qtd_1gp_s = 0
qtd_1gp_m = 0
segundo_gp = '17_to_25'
qtd_2gp_s = 0
qtd_2gp_m = 0
terceiro_gp = '26_to_39'
qtd_3gp_s = 0
qtd_3gp_m = 0
quarto_gp = '40_to_64'
qtd_4gp_s = 0
qtd_4gp_m = 0
quinto_gp = '65_to_74'
qtd_5gp_s = 0
qtd_5gp_m = 0
sexto_gp = '75_or_older'
qtd_6gp_s = 0
qtd_6gp_m = 0

for linha in linhas_separadas:
    if linha[-3] == primeiro_gp:
        if linha[6] == 'Single':
            qtd_1gp_s += 1
        elif linha[6] == 'Multiple':
            qtd_1gp_m += 1
    elif linha[-3] == segundo_gp:
        if linha[6] == 'Single':
            qtd_2gp_s += 1
        elif linha[6] == 'Multiple':
            qtd_2gp_m += 1
    elif linha[-3] == terceiro_gp:
        if linha[6] == 'Single':
            qtd_3gp_s += 1
        elif linha[6] == 'Multiple':
            qtd_3gp_m += 1
    elif linha[-3] == quarto_gp:
        if linha[6] == 'Single':
            qtd_4gp_s += 1
        elif linha[6] == 'Multiple':
            qtd_4gp_m += 1
    elif linha[-3] == quinto_gp:
        if linha[6] == 'Single':
            qtd_5gp_s += 1
        elif linha[6] == 'Multiple':
            qtd_5gp_m += 1
    elif linha[-3] == sexto_gp:
        if linha[6] == 'Single':
            qtd_6gp_s += 1
        elif linha[6] == 'Multiple':
            qtd_6gp_m += 1

print('Existem 2 tipos de acidente (Crash Type), o Single, isto é um acidente em que apenas um veículo está envolvido, e o Multiple, ou seja, quando há mais de um veículo envolvido no acidente')
print('A quantidade de acidentes do tipo Single ocorreu na seguinte frequência na Austrália, de acordo com a faixa etária de sua população: \n'
      'Entre 0 e 17: %d\n'
      'Entre 18 e 25: %d\n'
      'Entre 26 e 39: %d\n'
      'Entre 40 e 64: %d\n'
      'Entre 65 e 74: %d\n'
      'A partir de 75: %d'%(qtd_1gp_s,qtd_2gp_s,qtd_3gp_s,qtd_4gp_s,qtd_5gp_s,qtd_6gp_s))
print('Já a quantidade de acidentes do tipo Multiple ocorreu na seguinte frequência na Austrália, de acordo com a faixa etária de sua população: \n'
      'Entre 0 e 17: %d\n'
      'Entre 18 e 25: %d\n'
      'Entre 26 e 39: %d\n'
      'Entre 40 e 64: %d\n'
      'Entre 65 e 74: %d\n'
      'A partir de 75: %d'%(qtd_1gp_m,qtd_2gp_m,qtd_3gp_m,qtd_4gp_m,qtd_5gp_m,qtd_6gp_m))

x = [primeiro_gp,segundo_gp,terceiro_gp,quarto_gp,quinto_gp,sexto_gp]
y = [qtd_1gp_s,qtd_2gp_s,qtd_3gp_s,qtd_4gp_s,qtd_5gp_s,qtd_6gp_s]

sns.barplot(x=x, y=y)
plt.title('Frequência dos acidentes Single')
plt.show()

k = [primeiro_gp,segundo_gp,terceiro_gp,quarto_gp,quinto_gp,sexto_gp]
p = [qtd_1gp_m,qtd_2gp_m,qtd_3gp_m,qtd_4gp_m,qtd_5gp_m,qtd_6gp_m]

sns.barplot(x=k, y=p)
plt.title('Frequência dos acidentes Multiple')
plt.show()
