import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import numpy as np # Para manipulação de matrizes

def novaMatriz(matriz, incremento):
    matrizAntiga = matriz
    tamanhoMatrizAntiga = len(matriz)
    tamanhoMatrizNova = tamanhoMatrizAntiga + incremento

    matrizNova = np.zeros((tamanhoMatrizNova, tamanhoMatrizNova), dtype=np.float64)

    for i in range(tamanhoMatrizAntiga):
        for j in range(tamanhoMatrizAntiga):
            matrizNova[i][j] = matrizAntiga[i][j]

    return matrizNova

def arestas(matriz):

    while True:
        os.system('cls')
        try:
            escolha = int(input("""Opções de arestas:
                1 - Incluir arestas/arcos
                2 - Excluir arestas/arcos
                3 - Voltar às opções do grafo 
       Escolha: """))

            if escolha == 1:
                while True:
                    try:
                        os.system('cls')
                        v1 = int(input('Origem: '))
                        if(v1 > len(matriz) or v1 <= 0):
                            os.system('cls')
                            print(f'Desculpe... mas você inseriu uma origem inválida ({v1}).\n')
                            os.system('pause')
                            os.system('cls')
                            break
                        v2 = int(input('Destino: '))
                        if(v2 > len(matriz) or v1 <= 0):
                            os.system('cls')
                            print(f'Desculpe... mas você inseriu um destino inválido ({v2}).\n')
                            os.system('pause')
                            os.system('cls')
                            break
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
                    try:
                        os.system('cls')
                        v1 = int(input('Origem: '))
                        if(v1 > len(matriz) or v1 <= 0):
                            os.system('cls')
                            print(f'Desculpe... mas você inseriu um destino inválido ({v1}).\n')
                            os.system('pause')
                            os.system('cls')
                            break
                        v2 = int(input('Destino: '))
                        if(v2 > len(matriz) or v1 <= 0):
                            os.system('cls')
                            print(f'Desculpe... mas você inseriu um destino inválido ({v2}).\n')
                            os.system('pause')
                            os.system('cls')
                            break
                        matriz[v1-1][v2-1] = 0
                        n = int(input('Continuar ? [1]Sim [0]Nao '))
                        if n == 0:
                            os.system('cls')
                            break
                        if n == 1:
                            continue
                        else:
                            os.system('cls')
                            print(f'Você selecionou uma opção inválida ({n}), e por isso, interromperemos a exclusão de arestas/arcos.\n')
                            os.system('pause')
                            os.system('cls')
                            break
                    except ValueError:
                        os.system('cls')
                        print("Isso não é um número, interromperemos a exclusão de arestas/arcos.\n")
                        os.system('pause')
                        os.system('cls')
                        arestas(matriz)

            elif escolha == 3:
                os.system('cls')
                return matriz

            else:
                os.system('cls')
                print("Opção inválida. Tente novamente.\n")
                os.system('pause')
                os.system('cls')
        except ValueError:
            os.system('cls')
            print("Opção inválida. Tente novamente.\n")
            os.system('pause')
            os.system('cls')
            arestas(matriz)

def vertices(matriz):

    while True:
        try:
            os.system('cls')
            escolha = int(input("""Opções de vértices:
                1 - Incluir vertices
                2 - Excluir vertices
                3 - Voltar as opções do grafo
       Escolha: """))

            if escolha == 1:
                while True:
                    try:
                        os.system('cls')
                        v1 = int(input('Vértices a serem incluídos: '))
                        matriz = novaMatriz(matriz, v1)
                        n = int(input('Continuar ? [1]Sim [0]Nao '))
                        if n == 0:
                            os.system('cls')
                            break
                        elif n == 1:
                            continue
                        else:
                            os.system('cls')
                            print(f'Você selecionou uma opção inválida ({n}), e por isso, interromperemos a inclusão de vértices.\n')
                            os.system('pause')
                            os.system('cls')
                            break
                    except ValueError:
                        os.system('cls')
                        print("Opção inválida. Tente novamente.\n")
                        os.system('pause')
                        os.system('cls')
                        vertices(matriz)
                    
            elif escolha == 2:
                try:
                    while True:
                        os.system('cls')
                        v1 = int(input('Excluir vertice: '))
                        if(v1 > len(matriz) or v1 <= 0):
                            os.system('cls')
                            print(f'Desculpe... mas você inseriu um vertice inválido ({v1}).\n')
                            os.system('pause')
                            os.system('cls')
                            break
                        matriz = np.delete(matriz, (v1 - 1), axis=0)
                        matriz = np.delete(matriz, (v1 - 1), axis=1)
                        n = int(input('Continuar ? [1]Sim [0]Nao '))
                        if n == 0:
                            os.system('cls')
                            break
                        elif n == 1:
                            continue
                        else:
                            os.system('cls')
                            print(f'Você selecionou uma opção inválida ({n}), e por isso, interromperemos a inclusão de vértices.\n')
                            os.system('pause')
                            os.system('cls')
                            break
                except ValueError:
                        os.system('cls')
                        print("Isso não é um número, interromperemos a exclusão de vertices.\n")
                        os.system('pause')
                        os.system('cls')
                        vertices(matriz) 

            elif escolha == 3:
                os.system('cls')
                return matriz
            else:
                os.system('cls')
                print("Opção inválida. Tente novamente.\n")
                os.system('pause')
                os.system('cls')
        except ValueError:
            os.system('cls')
            print("Opção inválida. Tente novamente.\n")
            os.system('pause')
            os.system('cls')
            vertices(matriz)