"""
7. Escreva um algoritmo que solicite um número inteiro e exiba todos os divisores desse número.
"""

n = int(input('Digite um número inteiro: '))

print(f'Divisores de {n}: ')
for i in range(1, n+1):
    if n % i == 0:
        print(i)
