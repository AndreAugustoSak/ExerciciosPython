# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
 # par ou ímpar;
 # positivo ou negativo;
 # inteiro ou decimal.
def operacao():
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    oper = int(input('''Qual operação você deseja realizar?
Digite:
1 - soma
2 - subtração
3 - multiplicação
4 - divisão
'''))
    if oper == 1:
        resultado = n1 + n2
    elif oper == 2:
        resultado = n1 - n2
    elif oper == 3:
        resultado = n1 * n2
    elif oper == 4:
        resultado = n1 / n2
    if resultado % 2 == 0:
        tipo_1 = 'par'
    else:
        tipo_1 = 'ímpar'
    if resultado == round(resultado):
        tipo_2 = 'inteiro'
    else:
        tipo_2 = 'decimal'
    if resultado >= 0:
        tipo_3 = 'positivo'
    else:
        tipo_3 = 'negativo'
    print('O resultado é {} e este número é {}, {} e {}.'.format(resultado, tipo_1, tipo_2, tipo_3))
operacao()