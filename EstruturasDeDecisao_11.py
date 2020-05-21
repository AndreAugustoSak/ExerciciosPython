# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# - salários até R$ 280,00 (incluindo) : aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
## o salário antes do reajuste;
## o percentual de aumento aplicado;
## o valor do aumento;
## o novo salário, após o aumento.

def strutura_decisao_11():
    salario = float(input('Qual o salário do colaborador? (R$) '))
    if salario <= 280:
        percentual = 20
        aumento = salario * 0.2
        novo_salario = salario * 1.2
    if 281 < salario <= 700:
        percentual = 15
        aumento = salario * 0.15
        novo_salario = salario * 1.15
    if 701 < salario <= 1500:
        percentual = 10
        aumento = salario * 0.1
        novo_salario = salario * 1.1
    if salario > 1500:
        percentual = 5
        aumento = salario * 0.05
        novo_salario = salario * 1.05
    print('''Salário antes do reajuste: R$ {:.2f}
Percentual de aumento aplicado: {}%
Valor do aumento: R$ {:.2f}
Novo salário, após o aumento: R$ {:.2f}'''.format(salario, percentual, aumento, novo_salario))
strutura_decisao_11()
