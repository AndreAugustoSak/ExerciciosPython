# Faça um Programa que peça dois números e imprima o maior deles.
def estrutura_decisao_01():
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    if n1 > n2:
        print('{} é maior que {}.'.format(n1, n2))
    elif n1 < n2:
        print('{} é maior que {}.'.format(n2, n1))
    else:
        print('Os números são iguais.')
estrutura_decisao_01()
