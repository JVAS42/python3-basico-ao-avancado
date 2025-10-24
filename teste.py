def executa(funcao, *args):
    return funcao(*args)

soma = lambda x, y: x + y
print(soma(2, 2))

somav2 = executa(lambda x, y: x+y, 2, 3)
print(somav2)