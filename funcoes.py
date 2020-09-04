import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import numpy as np # Para manipulação de matrizes

def erro():
    os.system('cls')
    print("Opção inválida. Tente novamente.\n")
    os.system('pause')
    os.system('cls')

def buscaLarguraElemento(matriz):
    os.system('cls')
    print("Desculpe!! Ainda não implementamos essa funcionalidade!\n")
    os.system('pause')
    os.system('cls')
    buscaLargura(matriz)

def buscaProfundidadeElemento(matriz):
    os.system('cls')
    print("Desculpe!! Ainda não implementamos essa funcionalidade!\n")
    os.system('pause')
    os.system('cls')
    buscaLargura(matriz)

def buscaProfundidadeMostraVertices(matriz):
    os.system('cls')
    print("Desculpe!! Ainda não implementamos essa funcionalidade!\n")
    os.system('pause')
    os.system('cls')
    buscaLargura(matriz)

def buscaLarguraMostraVertices(matriz):
    os.system('cls')
    print("Desculpe!! Ainda não implementamos essa funcionalidade!\n")
    os.system('pause')
    os.system('cls')
    buscaLargura(matriz)

def buscaLargura(matriz):
    print("Bem vindo à busca em largura!\n")

    try:
        escolha = int(input("""Opções de BFS:
         1 - Buscar um elemento no grafo
         2 - Mostras todos os vértices em ordem de visitação
         3 - Voltar às opções do grafo 
Escolha: """))

        if escolha == 1:
            buscaLarguraElemento(matriz)

        elif escolha == 2:
            buscaLarguraMostraVertices(matriz)

        elif escolha == 3:
            os.system('cls')
            return 

        else:
            erro()

    except ValueError:
        erro()

    return matriz    

def buscaProfundidade(matriz):
    print("Bem vindo à busca em profundidade!\n")

    try:
        escolha = int(input("""Opções de DFS:
         1 - Buscar um elemento no grafo
         2 - Mostras todos os vértices em ordem de visitação
         3 - Voltar às opções do grafo 
Escolha: """))

        if escolha == 1:
            buscaProfundidadeElemento(matriz)

        elif escolha == 2:
            buscaProfundidadeMostraVertices(matriz)

        elif escolha == 3:
            os.system('cls')
            return 

        else:
            erro()

    except ValueError:
        erro()

    return matriz 

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
                            erro()
                            break
                        v2 = int(input('Destino: '))
                        if(v2 > len(matriz) or v1 <= 0):
                            erro()
                            break
                        matriz[v1-1][v2-1] = 1
                        n = int(input('Continuar ? [1]Sim [0]Nao '))
                        if n == 0:
                            os.system('cls')
                            break
                        elif n == 1:
                            continue
                        else:
                            erro()
                            break
                    except ValueError:
                        erro()
                        arestas(matriz)

            elif escolha == 2:
                while True:
                    try:
                        os.system('cls')
                        v1 = int(input('Origem: '))
                        if(v1 > len(matriz) or v1 <= 0):
                            erro()
                            break
                        v2 = int(input('Destino: '))
                        if(v2 > len(matriz) or v1 <= 0):
                            erro()
                            break
                        matriz[v1-1][v2-1] = 0
                        n = int(input('Continuar ? [1]Sim [0]Nao '))
                        if n == 0:
                            os.system('cls')
                            break
                        if n == 1:
                            continue
                        else:
                            erro()
                            break
                    except ValueError:
                        erro()
                        arestas(matriz)

            elif escolha == 3:
                os.system('cls')
                return matriz

            else:
                erro()
        except ValueError:
            erro()
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
                            erro()
                            break
                    except ValueError:
                        erro()
                        vertices(matriz)
                    
            elif escolha == 2:
                try:
                    while True:
                        os.system('cls')
                        v1 = int(input('Excluir vertice: '))
                        if(v1 > len(matriz) or v1 <= 0):
                            erro()
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
                            erro()
                            break
                except ValueError:
                    erro()
                    vertices(matriz) 

            elif escolha == 3:
                os.system('cls')
                return matriz
            else:
                erro()
        except ValueError:
            erro()
            vertices(matriz)