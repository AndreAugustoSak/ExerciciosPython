# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
 # - Salário Bruto até 900 (inclusive) - isento
 # - Salário Bruto até 1500 (inclusive) - desconto de 5%
 # - Salário Bruto até 2500 (inclusive) - desconto de 10%
 # - Salário Bruto acima de 2500 - desconto de 20%
def salario():
    valor_hora = float(input('Qual o valor da sua hora de trabalho? (R$) '))
    horas = float(input('Quantas horas você trabalhou no mês? '))
    bruto = valor_hora * horas
    if bruto <= 900:
        ir = 0
    elif 900 < bruto <= 1500:
        ir = 0.05
    elif 1500 < bruto <= 2500:
        ir = 0.10
    else:
        ir = 0.20
    inss = 0.10
    fgts = 0.11
    total_descontos = ir*bruto + inss*bruto
    liquido = bruto - total_descontos
    print('''
Salário Bruto (R$ {:.2f} * {}):   R$ {:.2f}
(-) IR ({:.0f}%):                       R$ {:.2f}
(-) INSS ({:.0f}%):                    R$ {:.2f}
FGTS ({:.0f}%):                        R$ {:.2f}
Total de descontos:                R$ {:.2f}
Salário líquido:                   R$ {:.2f}
'''.format(valor_hora, horas, bruto, ir*100,
               bruto*ir, inss*100, inss*bruto,
               fgts*100, fgts*bruto, total_descontos,
               liquido))
salario()
