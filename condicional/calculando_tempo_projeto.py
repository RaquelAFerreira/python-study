A = int(input('Informe os dias para a atividade A: '))
B = int(input('Informe os dias para a atividade B: '))
C = int(input('Informe os dias para a atividade C: '))

total = A+B+C

if A < 0 or B < 0 or C < 0:
    print('Erro Os dias não podem ser negativos.')
else:
    print(f'Tempo total do projeto = {total}')