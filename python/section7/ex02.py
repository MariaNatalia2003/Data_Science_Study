"""
Faça uma função que receba uma string e imprima esta string na forma vertical.
Por exemplo, se receber Python, deve imprimir:

P
y
t
h
o
n

"""

def string_vertical(palavra: str):
    for letra in palavra:
        print(letra + "\n")

string_vertical("coxinha")