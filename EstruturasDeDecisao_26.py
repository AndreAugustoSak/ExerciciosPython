# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
 # Álcool:
  # até 20 litros, desconto de 3% por litro
  # acima de 20 litros, desconto de 5% por litro
 # Gasolina:
  # até 20 litros, desconto de 4% por litro
 # acima de 20 litros, desconto de 6% por litro.
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
def combustivel():
    tipo = str(input('''Qual tipo de combustível você quer? 
Digite: 
A - para Álcool
G - para Gasolina
''')).strip().upper()
    litros = float(input('Quantos litros você quer abastecer? '))
    valor = 0
    if tipo == 'A' and litros <= 20:
        valor = litros * 1.9 * 0.97
        tipo = 'álcool'
    elif tipo == 'A' and litros > 20:
        valor = litros * 1.9 * 0.95
        tipo = 'álcool'
    elif tipo == 'G' and litros <= 20:
        valor = litros * 2.5 * 0.96
        tipo = 'gasolina'
    elif tipo == 'G' and litros > 20:
        valor = litros * 2.5 * 0.94
        tipo = 'gasolina'
    print('Para abastecer {} litros de {}, você deverá pagar R$ {:.2f}.'.format(litros, tipo, valor))
combustivel()