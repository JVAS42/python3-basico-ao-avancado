perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opcoes': ['1', '2', '3', '4'],
        'resposta': '4',
    },
    {
        'pergunta': 'Quem descobriu o Brasil?',
        'opcoes': ['Alberto', 'Bruno', 'Pedro', 'Casemiro'],
        'resposta': 'Pedro',
    },
    {
        'pergunta': 'Quantas copas do mundo Brasil tem?',
        'opcoes': ['5', '4', '7', '6'],
        'resposta': '5',
    }
]


def jogo_de_perguntas():
    acertos = 0
    erros = 0
    for i in range(0, len(perguntas)):
        print(perguntas[i]['pergunta'])
        for j in range(0, len(perguntas[i]['opcoes'])):
            print(f'{j} - {perguntas[i]['opcoes'][j]}')
        try:
            valor = int(input('Informe sua resposta: '))
            user_resposta = perguntas[i]['opcoes'][valor]
            if user_resposta == perguntas[i]['resposta']:
                print('Você acertou')
                acertos += 1
            else:
                print('Você errou')
                erros += 1
        except:
            print('Você errou')
            erros += 1
        
        print(f'Você acertou {acertos} e errou {erros} de {len(perguntas)} perguntas')

jogo_de_perguntas()