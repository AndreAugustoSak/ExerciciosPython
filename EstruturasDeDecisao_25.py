# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
 # "Telefonou para a vítima?"
 # "Esteve no local do crime?"
 # "Mora perto da vítima?"
 # "Devia para a vítima?"
 # "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
def inquerito():
    print('Responda SIM ou NÃO para as perguntas a seguir: ')
    p1 = str(input('Você telefonou para a vítima? ')).strip().upper()
    p2 = str(input('Você esteve no local do crime? ')).strip().upper()
    p3 = str(input('Você mora perto da vítima? ')).strip().upper()
    p4 = str(input('Você devia para a vítima? ')).strip().upper()
    p5 = str(input('Você já trabalhou com a vítima? ')).strip().upper()
    valor = 0
    if p1 == 'SIM':
        valor = valor + 1
    if p2 == 'SIM':
        valor = valor + 1
    if p3 == 'SIM':
        valor = valor + 1
    if p4 == 'SIM':
        valor = valor + 1
    if p5 == 'SIM':
        valor = valor + 1
    if valor == 5:
        print('Você é o(a) assassino(a)!')
    elif 3 <= valor <= 4:
        print('Você é cúmplice!')
    elif valor == 2:
        print('Você é suspeito(a)!')
    else:
        print('Você é inocente!')
inquerito()