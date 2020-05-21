# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
def estrutura_decisao_23():
    n = float(input('Digite um número qualquer: '))
    if n == round(n):
        print('{:.0f} é um número inteiro.'.format(n))
    else:
        print('{} é um número decimal.'.format(n))
estrutura_decisao_23()