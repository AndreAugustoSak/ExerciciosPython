# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
def estrutura_decisao_08():
    import numpy as np
    n1 = float(input('Qual o preço do primeiro produto? R$ '))
    n2 = float(input('Qual o preço do segundo produto? R$ '))
    n3 = float(input('Qual o preço do terceiro produto? R$ '))
    if n1 == n2 == n3:
        print('Os produtos todos têm o mesmo preço.')
    if n1 == n2 and n1 < n3:
        print('O primeiro e o segundo produtos são os mais baratos.')
    if n1 == n3 and n1 < n2:
        print('O primeiro e o terceiro produtos são os mais baratos.')
    if n2 == n3 and n1 > n2:
        print('O segundo e o terceiro produtos são os mais baratos.')
    if n1 < n2 and n1 < n3:
        print('O primeiro produto é o mais barato.')
    if n2 < n1 and n2 < n3:
        print('O segundo produto é o mais barato.')
    if n3 < n1 and n3 < n2:
        print('O terceiro protudo é o mais barato.')
estrutura_decisao_08()