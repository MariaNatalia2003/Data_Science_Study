"""
Crie um programa que leia o peso de uma carga em números inteiros. Se o peso for 
até 10kg, informe que o valor será de R$50,00. Entre 11 e 20kg, informe que o 
valor será de R$80,00. Se for maior que 20kg informe que o transporte não é 
aceito.
"""

def checa_peso(peso: float):
    carga_baixa = 50.00
    carga_media = 80.00

    if peso <= 10:
        print(f'O valor será de R${carga_baixa}.\n')
    # Não foi usado "peso >= 11" pois não abrangeria valores entre 10 e 11
    elif peso > 10 and peso <= 20:
        print(f'O valor será de R${carga_media}.\n')
    else:
        print("O transporte foi negado.\n")

checa_peso(12.78)
checa_peso(5.33)
checa_peso(17.9)
checa_peso(7.85)
checa_peso(50)