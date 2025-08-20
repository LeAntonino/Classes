from modulo import *
from time import sleep

print('-'*50)
print('CRIADOR DE OBJETOS'.center(50))
print('-'*50)
sleep(1)

while True:
    print('OPÇÕES:')
    print('[1] VER LISTA')
    print('[2] ADICIONAR OBJETO')
    print('[3] ALTERAR OBJETO')
    print('[4] DELETAR OBJETO')
    print('[5] SAIR')
    try:
        selecionador = int(input())
    except:
        print('valor inválido, tente novamente')
    if selecionador == 1:
        for i in range(0, len(Pessoa.listador)):
            print(f'{Pessoa.listador[i]}, Posição: {i}')
        if len(Pessoa.listador) == 0:
            print('A lista está vazia, adicione um objeto')
    elif selecionador == 2:
        Pessoa.criador(Pessoa.listador)
    elif selecionador == 3:
        Pessoa.substituidor(Pessoa.listador)
    elif selecionador == 4:
        Pessoa.deletador(Pessoa.listador)
    elif selecionador == 5:
        print('Até logo!')
        break