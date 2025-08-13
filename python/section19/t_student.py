"""
Distribuição T de Student

O teste T de Student é um teste estatístico usado para comparar as médias de 
duas amostras e determinar se a diferença entre elas é estatisticamente 
significativa. É frequentemente utilizado quando se trabalha com amostras 
pequenas e a variância populacional é desconhecida. 

O que é o teste T de Student?
O teste T de Student é um tipo de teste de hipótese que compara as médias de 
duas amostras. Ele é usado para avaliar se a diferença observada entre as médias 
é grande o suficiente para ser considerada estatisticamente significativa, ou se 
poderia ser explicada pelo acaso. 

Quando usar o teste T de Student?
O teste T de Student é particularmente útil quando:
- Você tem duas amostras independentes.
- A variância da população é desconhecida.
- Você tem tamanhos de amostra pequenos (geralmente menos de 30).
- Você deseja comparar as médias de duas amostras para ver se elas são 
significativamente diferentes. 

Tipos de testes T de Student:

- Teste T de Student para amostras independentes:
Compara as médias de duas amostras independentes (por exemplo, grupo de controle 
e grupo de tratamento). 
- Teste t de Student para amostras pareadas:
Compara as médias de duas amostras relacionadas (por exemplo, antes e depois do 
tratamento). 

Passos para realizar um teste T de Student:
1. Formular as hipóteses:
- Hipótese nula: Não há diferença significativa entre as médias das duas 
amostras. 
- Hipótese alternativa: Existe uma diferença significativa entre as médias das 
duas amostras. 
2. Escolher o nível de significância:
O nível de significância (alfa) é a probabilidade de rejeitar a hipótese nula 
quando ela é verdadeira (geralmente 0,05). 
3. Calcular a estatística T:
A fórmula para calcular a estatística T varia dependendo do tipo de teste T que 
você está usando. 
4. Determinar os graus de liberdade:
Os graus de liberdade são um parâmetro que afeta a distribuição T de Student e 
dependem do tamanho das amostras. 
5. Comparar a estatística T com o valor crítico:
Use uma tabela de distribuição T de Student ou um software estatístico para 
encontrar o valor crítico de T para seus graus de liberdade e nível de 
significância. 
6. Tomar uma decisão:
Se a estatística T calculada for maior que o valor crítico, rejeite a hipótese 
nula e conclua que existe uma diferença significativa entre as médias. 
Se a estatística T calculada for menor que o valor crítico, não rejeite a 
hipótese nula e conclua que não há evidências suficientes para afirmar que 
existe uma diferença significativa entre as médias. 
"""

# Importação da função
from scipy.stats import t

"""
Média de salário dos cientistas de dados: 75.00 por hora
Amostra com 9 funcionários
Desvio Padrão = 10
"""

# Probabilidade de selecionar um cientista de dados com salário menor que 80/h
# t.cdf(valor de t, graus de liberdade)
# cdf: olhar à esquerda da distribuição
menor_80 = t.cdf(1.5, 8)
print(menor_80)

# Probabilidade de selecionar um cientista de dados com salário maior que 80/h
# sf: olhar à direita da distribuição
maior_80 = t.sf(1.5, 8)
print(maior_80)

# Somatório das probabilidades
soma = menor_80 + maior_80
print(soma)