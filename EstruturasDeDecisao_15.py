# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
 # Dicas:
  # Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
  # Triângulo Equilátero: três lados iguais;
  # Triângulo Isósceles: quaisquer dois lados iguais;
  # Triângulo Escaleno: três lados diferentes.
def estrutura_decisao_15():
    l1 = float(input('Dê um lado de um triângulo: '))
    l2 = float(input('Dê o outro lado do triângulo: '))
    l3 = float(input('Dê o último lado do triângulo: '))
    if not l3 > (l1 + l2) and not l2 > (l1 + l3) and not l1 > (l2 + l3):
        if l1 != l2 != l3:
            print('As retas PODEM formar um triângulo ESCALENO.')
        elif l1 == l2 == l3:
            print('As retas PODEM formar um triângulo EQUILÁTERO.')
        else:
            print('As retas PODEM formar um triângulo ISÓSCELES.')
    else:
        print('As restas NÃO podem formar um triângulo.')
estrutura_decisao_15()