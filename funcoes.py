import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import numpy as np
import main

def arestas(matriz):
    os.system('cls')

    while True:
        try:
            escolha = int(input("""Opções de arestas:
                1 - Incluir arestas/arcos
                2 - Excluir arestas/arcos
                3 - Voltas às opções do grafo 
       Escolha: """))

            if escolha == 1:
                while True:
                    try:
                        os.system('cls')
                        v1 = int(input('Origem: '))
                        v2 = int(input('Destino: '))
                        matriz[v1-1][v2-1] = 1
                        n = int(input('Continuar ? [1]Sim [0]Nao '))
                        if n == 0:
                            os.system('cls')
                            break
                        elif n == 1:
                            continue
                        else:
                            os.system('cls')
                            print(f'Você selecionou uma opção inválida ({n}), e por isso, interromperemos a inclusão de arestas/arcos.\n')
                            os.system('pause')
                            os.system('cls')
                            break
                    except ValueError:
                        os.system('cls')
                        print("Isso não é um número, interromperemos a inclusão de arestas/arcos.\n")
                        os.system('pause')
                        os.system('cls')
                        arestas(matriz)

            elif escolha == 2:
                while True:
                    os.system('cls')
                    v1 = int(input('Origem: '))
                    v2 = int(input('Destino: '))
                    matriz[v1-1][v2-1] = 0
                    n = int(input('Continuar ? [1]Sim [0]Nao '))
                    if n == 0:
                        os.system('cls')
                        break

            elif escolha == 3:
                os.system('cls')
                main.opcoesGrafo(matriz)

            else:
                os.system('cls')
                print("Este número não está nas alternativas, tente novamente :D.\n")
                os.system('pause')
                os.system('cls')
        except ValueError:
            os.system('cls')
            print("Isso não é um número, tente novamente :D.\n")
            os.system('pause')
            os.system('cls')
            arestas(matriz)

    return matriz


def vertices(matriz):

    while True:
        os.system('cls')
        escolha = int(input("""Opções de vértices:
              1 - Incluir vertices
              2 - Excluir vertices
              3 - Sair 
     Escolha: """))

        if escolha == 1:
            while True:
                os.system('cls')
                v1 = int(input('Incluir vertice: '))
                #matriz[v1 - 1][v2 - 1] = 1
                n = int(input('Continuar ? [1]Sim [0]Nao '))
                if n == 0:
                    os.system('cls')
                    break

        elif escolha == 2:
            while True:
                os.system('cls')
                v1 = int(input('Excluir vertice: '))
                matriz = np.delete(matriz, (v1 - 1), axis=0)
                matriz = np.delete(matriz, (v1 - 1), axis=1)
                n = int(input('Continuar ? [1]Sim [0]Nao '))
                if n == 0:
                    os.system('cls')
                    break

        elif escolha == 3:
            os.system('cls')
            break

        else:
            os.system('cls')
            print("Este número não está nas alternativas, tente novamente :D.\n")

    return matriz
