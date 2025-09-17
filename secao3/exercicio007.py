try:
    valor_final = 0
    while True:
        resposta = input('INFROME [C] PARA continuar ou [S] sair: ').upper()
        if resposta == 'C':

            try:
                while True:
                    num1 = input('NÚMERO 1: ')
                    operador = input('OPERADOR: ')
                    num2 = input('NÚMERO 2: ')

                    num1 = int(num1)
                    num2 = int(num2)

                    if operador == '+':
                        valor_final = num1 + num2
                        print(f'{num1} + {num2}', end=' = ')
                        print(valor_final)
                        break
                    elif operador == '-':
                        valor_final = num1 - num2
                        print(f'{num1} - {num2}', end=' = ')
                        print(valor_final)
                        break
                    elif operador == '*':
                        valor_final = num1 * num2
                        print(f'{num1} * {num2}', end=' = ')
                        print(valor_final)
                        break
                    elif operador == '/':
                        valor_final = num1 / num2
                        print(f'{num1} + {num2}', end=' = ')
                        print(valor_final)
                        break
                    else:
                        print('ERRO, INFORME NOVAMENTE')
                        break
            except:
                print('ERRO, INFORME NOVAMENTE')

        elif resposta == 'S':
            break
        else:
            print('RESPOSTA INCORRETA, TENTE NOVAMENTE')
    print('CALCULADORA ENCERRADA!')
except:
    print('ERRO')