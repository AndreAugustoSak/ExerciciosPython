# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
def valida_data():
    import datetime
    data = str(input('Digite uma data no formato "dd/mm/aaaa": '))
    formato = '%d/%m/%Y'
    try:
        validacao = datetime.datetime.strptime(data, formato)
        print('{} é uma data válida.'.format(data))
    except ValueError:
        print('{} não é uma data válida.'.format(data))
valida_data()
