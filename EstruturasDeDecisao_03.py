# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
def sexo(n):
    n = str(input('Digite M para masculino e F para feminino: ')).upper().strip()
    if n == 'F':
        print('F - Feminino')
    elif n == 'M':
        print('M - Masculino')
    else:
        print('Sexo Inválido')
sexo(0)
