# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
 #                       Até 5 Kg           Acima de 5 Kg
 # Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
 # Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
def estrutura_decisao_27():
    maca = float(input('Quantos quilos de maçã você quer comprar? '))
    morango = float(input('Quantos quilos de morango você quer comprar? '))
    total_quilos = maca + morango
    valor_maca = 2.5
    valor_morango = 1.8
    if maca > 5:
        valor_maca = 2.2
    if morango > 5:
        valor_morango = 1.5
    custo_maca = maca * valor_maca
    custo_morango = morango * valor_morango
    custo_total = custo_maca + custo_morango
    if total_quilos >= 8 or custo_total >= 25:
        custo_total = custo_total * 0.9
    print('Você comprou {} quilo(s) de maça e {} quilo(s) de morango e o valor total a pagar é de R$ {:.2f}.'.format(maca, morango, custo_total))
estrutura_decisao_27()