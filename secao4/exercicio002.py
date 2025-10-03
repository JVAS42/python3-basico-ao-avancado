def duplicar(num):
    return num*2

def quadriplica(num):
    return 2*duplicar(num)

def triplicar(num):
    return 3*num

numero = int(input())

dobro = duplicar(numero)
triplo = triplicar(numero)
quadruplo = quadriplica(numero)

print(dobro, triplo, quadruplo)

# SOLUCAO #

def criar_multiplicador(multi):
    def multiplicar(num):
        return numero * multi
    return multi