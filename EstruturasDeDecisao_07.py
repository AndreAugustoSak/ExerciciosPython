# Faça um Programa que leia três números e mostre o maior e o menor deles.
def estrutura_decisao_07():
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    n3 = float(input('Digite o último número: '))
    list = [n1, n2, n3]
    print('O menor número é {} e o maior é {}.'.format(min(list), max(list)))
estrutura_decisao_07()