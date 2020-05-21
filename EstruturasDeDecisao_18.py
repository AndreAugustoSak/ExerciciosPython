# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
def strutura_decisao_18():
    import datetime
    data = str(input('Digite uma data no formato "dd/mm/aaaa": '))
    formato = '%d/%m/%Y'
    try:
        validacao = datetime.datetime.strptime(data, formato)
        print('{} é uma data válida.'.format(data))
    except ValueError:
        print('{} não é uma data válida.'.format(data))
strutura_decisao_18()
