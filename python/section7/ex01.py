"""
Faça um programa que tenha uma função chamada amplitude. A função deve receber 
uma lista e imprimir a amplitude. Crie também um código para testar sua função.
Amplitude: diferença entre o maior e menor número.
"""

def amplitude(numbers: list):
    min = numbers[0]
    max = numbers[0]

    for number in numbers:
        if number < min:
            min = number
        if number > max:
            max = number

    amp = max - min

    return amp

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [22, 5, 6, 3, 9, 5, 4]

res_amplitude = amplitude(list2)

print(res_amplitude)