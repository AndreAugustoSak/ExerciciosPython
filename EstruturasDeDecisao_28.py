# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
 #                       Até 5 Kg           Acima de 5 Kg
 # File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
 # Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
 # Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def estrutura_decisao_28():
    tipo = str(input('''Que tipo de carne você deseja comprar? 
Digite:
1 - para Filé Duplo
2 - para Alcatra
3 - para Picanha
'''))
    peso = float(input('Quantos quilos você quer comprar? '))
    cartao = str(input('''Como você prefere pagar? 
Digite:
1 - para Dinheiro
2 - para Cartão Tabajara
3 - para Cartão Normal
''')).strip().upper()
    valor = 0
    desconto = 0
    valor_final = 0
    if tipo == '1':
        tipo = 'Filé Duplo'
        valor = peso * 4.9
    elif tipo == '2':
        tipo = 'Alcatra'
        valor = peso * 5.9
    elif tipo == '3':
        tipo = 'Picanha'
        valor = peso * 6.9
    if peso > 5:
        valor = valor + peso * 0.9
    if cartao == '1':
        cartao = 'Dinheiro'
        desconto = 0
    elif cartao == '2':
        cartao = 'Cartão Tabajara'
        desconto = valor * 0.05
    elif cartao == '3':
        cartao = 'Cartão Normal'
        desconto = 0
    valor_final = valor - desconto
    print('''---NOTA FISCAL---
Produto: {}
Quantidade: {} quilo(s)
Preço Total: R$ {:.2f}
Tipo do Pagamento: {}
Valor do Desconto: R$ {:.2f}
Valor a Pagar: R$ {:.2f}
-----------------'''.format(tipo, peso, valor, cartao, desconto, valor_final))
estrutura_decisao_28()