vitoria = True
tentativas = 0
palavra = 'bola'
formatada = '*'*len(palavra)

while vitoria:
    if palavra.lower() == formatada:
        vitoria = False
    else:
        tentativas += 1
        letra = input('Digite uma letra: ')
        if len(letra) > 1 or letra.isdigit():
            print('Digite apenas uma letra')
        else:
            if letra in palavra.lower() and len(letra) == 1:
                for i in range(0, len(palavra)):
                    if letra == palavra[i]:
                        formatada = formatada[:i] + letra + formatada[i+1:]
                        print(f'Palavra formatada: {formatada}')
            else:
                print(f'Palavra formatada: {formatada}')


print('VOCÊ GANHOU! PARABÉNS')
print(f'A PALAVRA ERA {palavra}')
print(f'TENTATIVAS {tentativas}')