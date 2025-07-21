primeiro_valor = input('Informe o primeiro valor: ')
segundo_valor = input('Informe o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}')
elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor=} é maior que {primeiro_valor=}')
else:
    print(f'O {primeiro_valor=} é igual ao {segundo_valor=}')
