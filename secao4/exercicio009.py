# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def listar(lista_tarefas):
    print()
    if not lista_tarefas:
        print('Lista vazia')
        return
    
    print('TAREFAS:')
    for tarefa in lista_tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(lista_tarefas, lixo):
    print()
    if not lista_tarefas:
        print('Lista vazia')
        return
    
    tarefa = lista_tarefas.pop()
    print(f'{tarefa} removida da lista de tarefas.')
    lixo.append(tarefa)
    print()


def refazer(lista_tarefas, lixo):
    print()
    if not lixo:
        print('O lixo está vazio')
        return
    
    tarefa = lixo.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    lista_tarefas.append(tarefa)
    print()


def adicionar(tarefa, lista_tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    lista_tarefas.append(tarefa)
    print()


def importa(lista_tarefas):
    with open("lista.txt", "w", encoding="utf-8") as arquivo:
            for tarefa in lista_tarefas:
                arquivo.write(tarefa + "\n")
    print("Lista de tarefas importadas")


lista_tarefas = list()
lixo = list()

while True:
    print('COMANDOS\n1. [LISTAR]\n2. [DESFAZER]\n3. [REFAZER]\n4. [IMPORTAR]')
    tarefa = input('Informe um tarefa ou comando: ')

    if tarefa == 'listar':
        listar(lista_tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(lista_tarefas, lixo)
        listar(lista_tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(lista_tarefas, lixo)
        listar(lista_tarefas)
        continue
    elif tarefa == 'importar': # EXTRA
        importa(lista_tarefas)
        break
    else:
        adicionar(tarefa, lista_tarefas)
        listar(lista_tarefas)
        continue

