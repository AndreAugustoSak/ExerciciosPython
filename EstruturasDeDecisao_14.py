# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
 # - Média de Aproveitamento  Conceito
 # - Entre 9.0 e 10.0        A
 # - Entre 7.5 e 9.0         B
 # - Entre 6.0 e 7.5         C
 # - Entre 4.0 e 6.0         D
 # - Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def strutura_decisao_14():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunta nota: '))
    m = (n1 + n2) / 2
    if 9 < m <= 10:
        conceito = 'A'
    elif 7.5 < m <= 9:
        conceito = 'B'
    elif 6 < m <= 7.5:
        conceito = 'C'
    elif 4 < m <= 6:
        conceito = 'D'
    elif 0 <= m <= 4:
        conceito = 'E'
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        situacao = 'APROVADO'
    if conceito == 'D' or conceito == 'E':
        situacao = 'REPROVADO'
    print('''Nota um: {}
Nota dois: {}
Média: {}
Conceito: {}
Situação: {}'''. format(n1, n2, m, conceito, situacao))
strutura_decisao_14()
