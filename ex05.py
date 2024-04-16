"""
5. Escreva um algoritmo que solicite quinze números informados pelo usuário e exiba a raiz quadrada
de cada número (Dica: importe a biblioteca math).
"""

from math import sqrt

for i in range(1, 16):
    n = int(input(f'Digite o {i}o número: '))
    print(f'Raíz quadrada de {n}: {sqrt(n):.2f}')
