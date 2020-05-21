# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
def estrutura_decisao_21():
    valor = int(input('Qual o valor do saque? '))
    notas_100 = valor // 100
    notas_50 = (valor - notas_100 * 100) // 50
    notas_10 = (valor - notas_100 * 100 - notas_50 * 50) // 10
    notas_5 = (valor - notas_100 * 100 - notas_50 * 50 - notas_10 * 10) // 5
    notas_1 = valor - notas_100 * 100 - notas_50 * 50 - notas_10 * 10 - notas_5 * 5
    print('''Para sacar R$ {}, a máquina disponibilizará:
{} nota(s) de R$ 100,00;
{} nota(s) de R$ 50,00;
{} nota(s) de R$ 10,00;
{} nota(s) de R$ 5,00;
{} nota(s) de R$ 1,00.'''.format(valor, notas_100, notas_50, notas_10, notas_5, notas_1))
estrutura_decisao_21()