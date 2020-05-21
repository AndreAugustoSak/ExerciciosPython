# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
def estrutura_decisao_17():
    ano = int(input('Que ano quer analisar? '))
    if ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0:
        print('O ano {} é BISSEXTO.'.format(ano))
    else:
        print('O ano {} NÃO é BISSEXTO.'.format(ano))
estrutura_decisao_17()
