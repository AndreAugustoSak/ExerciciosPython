# Faça um Programa que leia três números e mostre-os em ordem decrescente.
def estrutura_decisao_09():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    list = [n1, n2, n3]
    ordem = sorted(list, reverse=True)
    print('A ordem decrescente dos número é :', ordem)
estrutura_decisao_09()
