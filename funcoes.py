### Autores
# Lucas Stofella da silva
# Stephen Michael Apolinário
# Wesley Grignani

import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import numpy as np # Para manipulação de matrizes
import main # Para voltar ao script principal

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

def buscarLinhasEmLargurasVertice(matriz, visited, queue, i):
    # Vai procurar algum elemento com valor = 1 e que não esteja visitado...
    # Na linha que foi nos passado.
    for j in range(len(matriz)):
        if(matriz[i][j] == 1 and j not in visited):
            queue.append(j)

    # Se a fila estiver vazia...
    if(queue == []):
        for x in range (len(matriz)):
            if(x not in visited):
                visited.append(x)
                buscarLinhasEmLargurasVertice(matriz, visited, queue, x)
        # Se não encontrou nenhuma linha não visitada, acabou o programa.
        for index in range(len(visited)): 
            visited[index] = visited[index] + 1 
        os.system('cls')
        print('TERMINOU!\n')
        print(visited)
        os.system('pause')
        os.system('cls')
        buscaLargura(matriz)
    
    # Se ainda não terminou de percorrer em largura, e ainda tenho elementos na fila...
    elif(queue != []):
        for element in queue:
            if(element not in visited):
                visited.append(element)
                # tira elemento da fila
        novoElemento = queue[0]
        del queue[0]
        buscarLinhasEmLargurasVertice(matriz, visited, queue, novoElemento)

def buscaLarguraMostraVertices(matriz):
    os.system('cls')

    visited = []
    queue = []
    # Usuário escolhe a linha - 1
    try:
        i = int(input("Escolha um vértice para iniciar: ")) - 1
        if(i > len(matriz) or i < 0):
            erro()
            buscaLarguraMostraVertices(matriz)

    except ValueError:
        erro()
        buscaLarguraMostraVertices(matriz)

    visited.append(i)

    buscarLinhasEmLargurasVertice(matriz, visited, queue, i)

def buscaProfundidadeElemento(matriz):
    os.system('cls')
    print("Desculpe!! Ainda não implementamos essa funcionalidade!\n")
    os.system('pause')
    os.system('cls')
    buscaLargura(matriz)

def buscaProfundidadeMostraVertices(matriz):
    os.system('cls')
    visitados = np.zeros(len(matriz))  # vetor de elementos visitados

    escolha = int(input("""
        Informe o vertice de origem: """))

    if escolha <= len(matriz):
        quant_linhas = len(matriz)  # Conta quantas linhas existem
        quant_colunas = len(matriz[0])  # Conta quantos elementos têm em uma linha
        escolha -= 1
        visitados[escolha] = 1  # Primeiro vertice visitado
        pilha = []  # Criação da pilha

        pilha.append(escolha)  # primeiro elemento escolhido visitado
        inicio = escolha  # iniciando pela linha do elemento escolhido da matriz
        parada = 0  # criterio de parada
        caminho = []  # vetor reservado para guardar o caminho percorrido
        caminho.append(escolha+1)  # inicio do caminho


        while parada == 0:  # criterio de parada
            contador = 0
            for j in range(quant_colunas):  # percorrer a matriz em busca de um elemento nao visitado
                if matriz[inicio][j] == 1 and visitados[j] == 0:
                    pilha.append(j)  # adiciona na pilha
                    visitados[j] = 1  # marca elemento como visitado
                    inicio = int(j)  # define este elemento como principal
                    caminho.append(j+1)  # adiciona elemento no vetor de caminhos
                    break
                else:
                    contador += 1  # caso nao encontre um vertice nao visitado

            if visitados.mean() == 1:  # se vetor de visitados estiver cheio codigo termina
                parada = 1  # altera o criterio de parada
                print(caminho)  # mostra o caminho feito
                keyboard.wait('esc')

            elif contador == len(matriz):  # caso tenha percorrido toda linha e nao encontrou vertice nao visitado
                if len(pilha) == 0:  # se a pilha estiver vazia
                    for y in range(quant_colunas):  # procura por vertices ainda nao visitados
                        if visitados[y] == 0:
                            inicio = int(y)
                            visitados[y] = 1
                            caminho.append(y+1)
                            pilha.append(y)
                            break
                else:  # caso a pilha esteja com algum vertice
                    inicio = pilha.pop()

    else:
        os.system('cls')
        print('Valor invalido!!')
        keyboard.wait('esc')
        buscaProfundidadeMostraVertices(matriz)


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
            return main.opcoesGrafo(matriz)
        else:
            erro()
            return main.opcoesGrafo(matriz)

    except ValueError:
        erro()
        main.opcoesGrafo(matriz)

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
            return main.opcoesGrafo(matriz) 

        else:
            erro()
            return main.opcoesGrafo(matriz) 

    except ValueError:
        erro()
        return main.opcoesGrafo(matriz) 

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