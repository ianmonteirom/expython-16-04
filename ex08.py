"""
8. Escreva um algoritmo que determine se um número N (informado pelo usuário) é primo ou não.
"""

n, divs = 0, 0

while n <= 1:
    n = int(input('Digite um número inteiro maior que 1: '))

for i in range(1, n+1):
    if n % i == 0:
        divs += 1

if divs > 2:
    print(f'{n} NÃO é primo.')
else:
    print(f'{n} É primo.')
