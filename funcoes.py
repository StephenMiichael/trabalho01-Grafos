### Autores
# Lucas Stofella da silva
# Stephen Michael Apolinário
# Wesley Grignani

import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import numpy as np # Para manipulação de matrizes
import main # Para voltar ao script principal
import erro # Para mostrar mensagens de erro

def buscaLarguraElemento(matriz):
    os.system('cls')
    print("Desculpe!! Ainda não implementamos essa funcionalidade!\n")
    os.system('pause')
    os.system('cls')
    buscaLargura(matriz)

def buscarLinhasEmLargurasVertice(matriz, visited, queue, i):
    # Irá percorer todas as colunas da nossa linha passada pelo usuário.
    for j in range(len(matriz)):
        # Caso encontre valores = 1, e que estes não estejam nos visitados.
        if(matriz[i][j] == 1 and j not in visited):
            # Irá adicionar no final da lista de fila, os valores do vértice com ligações.
            queue.append(j)

    # Se a fila estiver vazia.
    if(queue == []):
        # Irá procurar um novo vértice (Linha) de nossa matriz.
        for x in range (len(matriz)):
            # Se a linha não estiver nos visitados.
            if(x not in visited):
                # Irá adicionar o vértice (Linha) no final dos visitados.
                visited.append(x)
                # Irá chamar a função novamente.
                buscarLinhasEmLargurasVertice(matriz, visited, queue, x)
        # Se não encontrou nenhuma linha não visitada, acabou a busca.
        for index in range(len(visited)): 
            # Apenas para melhoria visual aos usuários, será tratado os valores;
            # Da lista de visitados, para + 1.
            visited[index] = visited[index] + 1
        # Limpa a tela
        os.system('cls')
        print('TERMINOU!\n')
        # Irá printar a nossa lista de visitados em ordem.
        print(visited)
        # Irá dar um pause no terminal, e depois limpar a tela.
        os.system('pause')
        os.system('cls')
        # Irá voltar para as opções de busca em largura, passando a matriz.
        buscaLargura(matriz)
    
    # Se a fila não está vazia.
    elif(queue != []):
        # Para cada elemento da fila.
        for element in queue:
            # Se o elemento não estiver nos visitados.
            if(element not in visited):
                # Irá adiciopnar o elemento da fila no final dos visitados.
                visited.append(element)
        # Irá criar uma variável auxiliar para pegar o primeiro valor da fila.
        novoElemento = queue[0]
        # Irá deletar o primeiro valor da fila.
        del queue[0]
        # Irá chamar a nossa função novamente, mas agora irá passar o valor do;
        # Novo elemento.
        buscarLinhasEmLargurasVertice(matriz, visited, queue, novoElemento)

# Função de mostrar todos os vértices de uma matriz em ordem de visitação
# Através de uma busca em largura
def buscaLarguraMostraVertices(matriz):
    # Limpa a tela.
    os.system('cls')

    # Inicia duas lists em branco;
    # Uma lista será a nossa fila, e outra a de vértices visitados.
    visited = []
    queue = []
    try:
        # Usuário escolhe a linha - 1
        i = int(input("Escolha um vértice para iniciar: ")) - 1

        # Se o valor que o usuário digitar -1 for maior que a dimensão da matriz;
        # Ou então se o valor for menor que 0.
        if(i > len(matriz) or i < 0):
            # Irá mostrar uma mensagem de erro genérico.
            erro.mensagem()
            # Irá retornar a nossa função, para limpar a tela e perguntar por; 
            # Qual vértice começar.
            buscaLarguraMostraVertices(matriz)

    # Se o valor que o usuário digitar não for um inteiro.
    except ValueError:
        # Irá mostrar uma mensagem de erro genérico.
        erro.mensagem()
        # Irá retornar a nossa função, para limpar a tela e perguntar por; 
        buscaLarguraMostraVertices(matriz)

    # Caso passe pelas verificações, irá adicionar no final da lista de visitados;
    # O valor de entrada pelo usuário.
    visited.append(i)

    # E irá chamar a função que vai mostrar os vértices em ordem de visitação;
    # Através de uma busca em largura.
    # A função passa como parametro a própria matriz, a lista de visitados (Que contem;
    # O valor adicionado pelo usuário), a lista de fila, e o próprio valor inserido
    # Que será a nossa linha. 
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
            erro.mensagem()
            return main.opcoesGrafo(matriz)

    except ValueError:
        erro.mensagem()
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
            erro.mensagem()
            return main.opcoesGrafo(matriz) 

    except ValueError:
        erro.mensagem()
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
                            erro.mensagem()
                            break
                        v2 = int(input('Destino: '))
                        if(v2 > len(matriz) or v1 <= 0):
                            erro.mensagem()
                            break
                        matriz[v1-1][v2-1] = 1
                        n = int(input('Continuar ? [1]Sim [0]Nao '))
                        if n == 0:
                            os.system('cls')
                            break
                        elif n == 1:
                            continue
                        else:
                            erro.mensagem()
                            break
                    except ValueError:
                        erro.mensagem()
                        arestas(matriz)

            elif escolha == 2:
                while True:
                    try:
                        os.system('cls')
                        v1 = int(input('Origem: '))
                        if(v1 > len(matriz) or v1 <= 0):
                            erro.mensagem()
                            break
                        v2 = int(input('Destino: '))
                        if(v2 > len(matriz) or v1 <= 0):
                            erro.mensagem()
                            break
                        matriz[v1-1][v2-1] = 0
                        n = int(input('Continuar ? [1]Sim [0]Nao '))
                        if n == 0:
                            os.system('cls')
                            break
                        if n == 1:
                            continue
                        else:
                            erro.mensagem()
                            break
                    except ValueError:
                        erro.mensagem()
                        arestas(matriz)

            elif escolha == 3:
                os.system('cls')
                return matriz

            else:
                erro.mensagem()
        except ValueError:
            erro.mensagem()
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
                            erro.mensagem()
                            break
                    except ValueError:
                        erro.mensagem()
                        vertices(matriz)
                    
            elif escolha == 2:
                try:
                    while True:
                        os.system('cls')
                        v1 = int(input('Excluir vertice: '))
                        if(v1 > len(matriz) or v1 <= 0):
                            erro.mensagem()
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
                            erro.mensagem()
                            break
                except ValueError:
                    erro.mensagem()
                    vertices(matriz) 

            elif escolha == 3:
                os.system('cls')
                return matriz
            else:
                erro.mensagem()
        except ValueError:
            erro.mensagem()
            vertices(matriz)