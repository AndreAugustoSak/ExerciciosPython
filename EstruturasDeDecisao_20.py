# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
 # A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
 # A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
 # A mensagem "Aprovado com Distinção", se a média for igual a 10.
def estrutura_decisao_20():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunta nota: '))
    n3 = float(input('Digite a terceira nota: '))
    m = (n1 + n2 + n3) / 3
    if m == 10:
        print('Sua média foi 10 e você foi APROVADO COM DISTINÇÃO.')
    elif 7 <= m <= 9.9:
        print('Sua média foi {:.2f} e você foi APROVADO.'.format(m))
    else:
        print('Sua média foi {:.2f} e você foi REPROVADO.'.format(m))
estrutura_decisao_20()