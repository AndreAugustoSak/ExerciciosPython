# Faça um Programa que leia três números e mostre o maior deles.
def estrutura_decisao_06():
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite um outro número: '))
    n3 = float(input('Digite o último número: '))
    lista = [n1, n2, n3]
    print('O maior número é {}.'.format(max(lista)))
estrutura_decisao_06()