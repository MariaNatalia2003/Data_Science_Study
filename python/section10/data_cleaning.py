"""
Tratar dados 'tempo.csv'

Escopo:
    - Aparência: sol, nublado, chuva
    - Temperatura: -130 ~ 130 F
    - Umidade: 0 ~ 100
    - Jogar: sim/nao

Tratar valores NAs
"""

# Importação de Bibliotecas
import pandas as pd
import seaborn as srn
import statistics as sts

TEMPO_PATH = r"C:\Users\maria_cardim\Desktop\Data_Science\python\section10\tempo.csv"

# Leitura do arquivo csv
dataset = pd.read_csv(TEMPO_PATH, sep=";")
# Visualização das cinco primeiras linhas do dataset
print(dataset.head())

# Verifica o tamanho do dataset
print(dataset.shape)

# Agrupamento da coluna "Aparencia" para análise
grupo_aparencia = dataset.groupby(['Aparencia']).size()
print()
print(grupo_aparencia)

# Na coluna "Aparencia", tem um valor "menos", que não faz parte do escopo da 
# análise. Para resolver, vamos incluir esse valor em "chuva" ou "sol", que é a 
# moda da coluna (valor que mais aparece). O escolhido foi "chuva".

# Alteração do valor no dataset
dataset.loc[dataset['Aparencia'] == 'menos', 'Aparencia'] = "chuva"
# Visualização da coluna agrupada para ver se funcionou
grupo_aparencia = dataset.groupby(['Aparencia']).size()
print()
print(grupo_aparencia)

# Verificação se tem valores vazios na coluna "Aparencia"
aparencia_vazios = dataset['Aparencia'].isnull().sum()
print()
print(aparencia_vazios)

# Agrupamento da coluna "Temperatura" para análise
grupo_temperatura = dataset.groupby(['Temperatura']).size()
print()
print(grupo_temperatura)

# Verificação se tem valores vazios na coluna "Temperatura"
temperatura_vazios = dataset['Temperatura'].isnull().sum()
print()
print(temperatura_vazios)

# Cálculo da mediana para limpar o valor fora do limite na "Temperatura"
mediana_temp = sts.median(dataset['Temperatura'])
print()
print(mediana_temp)

# Substituição do valor da mediana nos campos de "Temperatura" fora dos limites
# Importante utilizar o valor inteiro da mediana para preservar o tipo da coluna
dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130), 'Temperatura'] = int(mediana_temp)

# Verificação se existe algum valor fora do escopo
print(dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130)])

# Agrupamento da coluna "Temperatura" para visualizar se o valor foi substituído
grupo_temperatura = dataset.groupby(['Temperatura']).size()
print()
print(grupo_temperatura)

# Agrupamento da coluna "Umidade" para análise
grupo_umidade = dataset.groupby(['Umidade']).size()
print()
print(grupo_umidade)

# Verificação se tem valores vazios na coluna "Umidade"
umidade_vazios = dataset['Umidade'].isnull().sum()
print()
print(umidade_vazios)

# Cálculo da mediana para limpar o valor fora do limite na "Umidade"
mediana_umidade = sts.median(dataset['Umidade'])
print()
print(mediana_umidade)

# Substituição do valor da mediana nos campos de "Umidade" fora dos limites
# Importante utilizar o valor inteiro da mediana para preservar o tipo da coluna
dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100), 'Umidade'] = int(mediana_umidade)

# Verificação se existe algum valor fora do escopo
print(dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100)])

# Preenche NAs com o valor da mediana
# inplace significa que substituirá no próprio dataset
# dataset['Umidade'].fillna(int(mediana_umidade), inplace=True)
# Este método não funcionará a partir do pandas 3.0
dataset['Umidade'] = dataset['Umidade'].fillna(int(mediana_umidade))

# Agrupamento da coluna "Umidade" para analisar se o valor foi substituído e o 
# campo vazio preenchido
grupo_umidade = dataset.groupby(['Umidade']).size()
print()
print(grupo_umidade)

# Agrupamento da coluna "Vento" para análise
grupo_vento = dataset.groupby(['Vento']).size()
print()
print(grupo_vento)

# Verificação se tem valores vazios na coluna "Vento"
vento_vazios = dataset['Vento'].isnull().sum()
print()
print(vento_vazios)

# Preenchimento do valor vazio com "FALSO", que é a moda da coluna
dataset['Vento'] = dataset['Vento'].fillna("FALSO")

# Agrupamento da coluna "Vento" para analisar se o valor foi preenchido
grupo_vento = dataset.groupby(['Vento']).size()
print()
print(grupo_vento)

# Agrupamento da coluna "Jogar" para analisar se o valor foi substituído
grupo_jogar = dataset.groupby(['Jogar']).size()
print()
print(grupo_jogar)

# Verificação se tem valores vazios na coluna "Jogar"
jogar_vazios = dataset['Jogar'].isnull().sum()
print()
print(jogar_vazios)

# Coluna "Jogar" não precisa de tratamentos.
# Análise do dataset limpo
print()
print(dataset)