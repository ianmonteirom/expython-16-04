"""
6. Criar um algoritmo que leia dez números inteiros e informe o maior e o menor número.
"""

maior = 0
menor = 9999999999

for i in range(1, 11):
    n = int(input(f'Digite o {i}o número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'Maior número: {maior}\n'
      f'Menor número: {menor}')
