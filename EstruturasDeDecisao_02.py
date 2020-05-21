# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
def estrutura_decisao_02():
    n = float(input('Digite um número: '))
    if n < 0:
        print('O número {} é negativo.'.format(n))
    else:
        print('O número {} é positivo.'.format(n))
estrutura_decisao_02()
