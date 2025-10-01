# MULTIPLICAÇÃO #

def mult(*args):
    multiplicacao = 1
    for numero in args:
        multiplicacao *= numero
    return multiplicacao

numeros = input().split()
numeros = tuple(map(float, numeros))
total = mult(*numeros)

print(f'O TATAL DA MULTIPLICAÇÃO = {total:.2f}')

# PAR OU IMPAR #
def verifica(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
try:
    numero = input('Informe um valor: ')
    numero = int(numero)
    print(f'O NÚMERO {numero} É {verifica(numero)}')
except:
    print('ERRO')