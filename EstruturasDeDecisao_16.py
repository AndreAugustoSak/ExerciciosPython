# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
 # Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
 # Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
 # Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
 # Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário.
def bhaskara():
    a = float(input('Qual o valor de A? '))
    if a == 0:
        print('Não é uma equação de segundo grau.')
        exit()
    b = float(input('Qual é o valor de B? '))
    c = float(input('Qual é o valor de C? '))
    delta = b**2 - 4*a*c
    if delta < 0:
        print('A equação não possui raízes reais.')
        exit()
    elif delta == 0:
        raiz = -b/(2*a)
        print('A equação possui uma raiz igual a {:.3f}.'.format(raiz))
    else:
        raiz1 = (-b + (delta**(1/2)))/(2*a)
        raiz2 = (-b - (delta**(1/2)))/(2*a)
        print('A raiz x1 da equação é {:.3f}.'.format(raiz1))
        print('A raiz x2 da equação é {:.3f}.'.format(raiz2))
bhaskara()