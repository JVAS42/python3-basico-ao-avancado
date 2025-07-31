nome = str(input('Informe seu nome: '))

if nome != "":
    idade = int(input('Informe sua idade: '))
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if " " in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaço')
    print(f'A primeira letra do seu nome é {nome[0]}')
else:
    print('Desculpa, você deixou campos vazios.')