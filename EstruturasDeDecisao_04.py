# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
def estrutura_decisao_04():
    n = str(input('Digite uma letra: ')).strip().upper()
    if n.isalpha():
        if n in 'AEIOU':
            print('{} é uma vogal.'.format(n))
        else:
            print('{} é uma consoante.'.format(n))
    else:
        print('{} não é uma letra.'.format(n))
estrutura_decisao_04()