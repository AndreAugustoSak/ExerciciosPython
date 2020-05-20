# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
def numero():
    n = int(input('Informe um número inteiro: '))
    if n % 2 == 0:
        print('{} é um número par.'.format(n))
    else:
        print('{} é um número ímpar.'.format(n))
numero()