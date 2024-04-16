"""
10. Solicite a quantidade de alunos de uma turma e a quantidade de notas. Para cada aluno, solicite as
suas notas e exiba a sua respectiva média.
"""

qnt_alunos = int(input('Quantidade de alunos: '))
qnt_notas = int(input('Quantidade de notas: '))

for i in range(1, qnt_alunos+1):
    soma_notas = 0
    for p in range(1, qnt_notas+1):
        nota = float(input(f'{p}a nota do {i}o aluno: '))
        soma_notas += nota
    media = soma_notas / qnt_notas
    print('--' * 24)
    print(f'Média do {i}o aluno: {media:.2f}')
    print('--' * 24)

