# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
def estrutura_decisao_19():
    import __future__
    n = int(input('Digite um número inteiro menor que mil: '))
    if n >= 1000 or n < 0:
        print('Numero inválido!')
        estrutura_decisao_19()
    else:
        print(n, '=', ''.join(list(filter(lambda p: p, ['' if x[0] == '0'
else ', ' + ' '.join(x)+('' if x[0] == '1' else 's') for x in
zip(str(n)[::-1], ('centena', 'dezena',
'unidade')[::-1])]))[::-1])[2:][::-1].replace(' ,', ' e ', 1)[::-1])
estrutura_decisao_19()