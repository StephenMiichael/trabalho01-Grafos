# Autores
# Lucas Stofella da silva
# Stephen Michael Apolinário
# Wesley Grignani

import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import main  # Para voltar ao script principal
import funcoes  # Para mostrar as mensagens de erro
import numpy as np  # Para manipulação de matrizes
import erro  # Para mostrar mensagens de erro


def verificaSubrafos(matriz, subgrafos):
    for i in range(len(matriz)):
        if i not in (item for sublist in subgrafos for item in sublist):
            return i


def buscaFechosTransitivos(matriz, verticeIniciador):
    # Matriz Exemplo 1
    # matriz[0][1] = 1
    # matriz[0][4] = 1
    # matriz[1][0] = 1
    # matriz[1][2] = 1
    # matriz[1][4] = 1
    # matriz[2][1] = 1
    # matriz[2][3] = 1
    # matriz[2][4] = 1
    # matriz[3][1] = 1
    # matriz[3][2] = 1
    # matriz[3][4] = 1
    # matriz[4][0] = 1
    # matriz[4][2] = 1
    # matriz[4][3] = 1

    # Matriz Exemplo 2
    # matriz[0][1] = 1
    # matriz[0][3] = 1
    # matriz[1][2] = 1
    # matriz[2][6] = 1
    # matriz[3][4] = 1
    # matriz[3][5] = 1
    # matriz[4][0] = 1
    # matriz[4][1] = 1
    # matriz[4][2] = 1
    # matriz[4][6] = 1
    # matriz[5][2] = 1
    # matriz[6][1] = 1
    # matriz[6][5] = 1

    # Matriz Exemplo Slide
    matriz[0][4] = 1
    matriz[0][5] = 1
    matriz[1][6] = 1
    matriz[2][7] = 1
    matriz[4][8] = 1
    matriz[5][4] = 1
    matriz[5][8] = 1
    matriz[6][0] = 1
    matriz[7][3] = 1
    matriz[8][0] = 1

    subgrafos = []
    tamanhoSubgrafos = 0
    conexo = True

    while(True):
        print(f'Vertice Iniciador {verticeIniciador}')
        aux = []
        auxDireto = []
        auxIndireto = []
        direto = fechoTransitivoDireto(matriz, verticeIniciador)
        indireto = fechoTransitivoIndireto(matriz, verticeIniciador)

        print(f'Direto: {direto}')
        print(f'Indireto: {indireto}')

        for pos in range(len(direto)):
            if(direto[pos] != None):
                auxDireto.append(pos)

        for pos in range(len(indireto)):
            if(indireto[pos] != None):
                auxIndireto.append(pos)

        # Faz uma intersecção entre os valores de Direto e Indireto.
        aux = list(set(auxDireto) & set(auxIndireto))

        subgrafos.append(aux)

        print(f'Auxiliar Direto: {auxDireto}')
        print(f'Auxiliar Indireto: {auxIndireto}')
        print(f'Intersecção: {aux}')
        print(f'Subgrafos: {subgrafos}')

        # Verifica quantos vértices possui a soma de subrafos.
        for element in subgrafos:
            for x in element:
                tamanhoSubgrafos += 1

        print(f'Tamanho Subgrafo: {tamanhoSubgrafos}')
        os.system('pause')
        # Se e a quantidade de vértices nos subgrafos for diferente do tamanho
        # da matriz, então ainda teremos que fazer mais transições, e o grafo não
        # é conexo.
        if(tamanhoSubgrafos != len(matriz)):
            tamanhoSubgrafos = 0
            conexo = False
            verticeIniciador = verificaSubrafos(matriz, subgrafos)
        else:
            if(conexo == True):
                print("O seu grafo é conexo!")
            else:
                subgrafos = [s for s in subgrafos if len(s) != 1]
                print("O seu grafo não é conexo!")
            if(len(subgrafos) == 1):
                subgrafos = subgrafos[0]
            print(subgrafos)
            os.system('pause')
            break


def fechoTransitivoDireto(matriz, vertice):
    vetor = np.zeros(len(matriz))
    vetor[vertice] = -1
    vetor_aux = np.zeros(len(matriz))
    vetor_aux[vertice] = -1

    parada = 0

    quant_colunas = len(matriz[0])  # Conta quantos elementos têm em uma linha
    n = 1
    n_aux = 1

    while parada == 0:  # condição de parada para
        contador2 = 0
        parada2 = 0
        for j in range(quant_colunas):  # laço para percorrer toda a linha da matriz
            # verifica se o vertice possui alguma ligacao
            if matriz[vertice][j] == 1 and vetor[j] == 0:
                # adiciona o caminho no vetor de visitados e no vetor auxiliar
                vetor[j] = n

                # o vetor auxiliar é utilizado para posteriormente encontrar quem serao os proximos vertices
                # de caminho menor para percorrer
                vetor_aux[j] = n
            else:
                contador2 += 1

        if vetor_aux.mean() == -1:  # condição de parada criada para verificar quando o vetor auxiliar estiver cheio
            parada = 1

        # esta parte do codigo é destinada a percorrer o vetor auxiliar e encontrar sempre o vertice de caminho menor
        # para ser utilizado como novo vertice de origem no codigo acima
        parada3 = 0
        while parada2 == 0:
            contador = 0

            # caso o caminho tenha sido incrementado duas vezes e mesmo assim não foi encontrado vertices
            if parada3 == 2:
                parada = 1
                break

            # percorre o vetor auxiliar em busca de vertices de caminho menor
            for j in range(quant_colunas):
                if vetor_aux[j] == n_aux:
                    vertice = int(j)  # define a posicao do novo vertice
                    vetor_aux[j] = -1
                    n = n_aux + 1
                    parada2 = 1
                    break
                else:
                    contador += 1  # caso nao encontre algum vertice com o determinado valor de caminho

            # esta condicao é verdadeira quando nao existe mais vertices de caminho especifico procurado
            # e entao o caminho é incrementado
            if len(matriz) == contador:
                n_aux += 1
                parada3 += 1  # criterio de parada criado para verificar quantas vezes o caminho foi incrementado

    direto = [None]*len(matriz)
    for pos in range(len(vetor)):
        if(vetor[pos] == 0):
            direto[pos] = None
        elif(vetor[pos] == -1):
            direto[pos] = 0
        else:
            direto[pos] = vetor[pos].astype(np.int64)

    return direto


def fechoTransitivoIndireto(matriz, vertice):
    vetor = np.zeros(len(matriz))
    vetor[vertice] = -1
    vetor_aux = np.zeros(len(matriz))
    vetor_aux[vertice] = -1

    parada = 0

    quant_colunas = len(matriz[0])  # Conta quantos elementos têm em uma linha
    n = 1
    n_aux = 1

    while parada == 0:
        contador2 = 0
        parada2 = 0
        for j in range(quant_colunas):
            if matriz[j][vertice] == 1 and vetor[j] == 0:
                vetor[j] = n
                vetor_aux[j] = n
            else:
                contador2 += 1

        if vetor_aux.mean() == -1:
            parada = 1

        parada3 = 0
        while parada2 == 0:
            contador = 0

            if parada3 == 2:
                parada = 1
                break

            for j in range(quant_colunas):
                if vetor_aux[j] == n_aux:
                    vertice = int(j)
                    vetor_aux[j] = -1
                    n = n_aux + 1
                    parada2 = 1
                    break
                else:
                    contador += 1

            if len(matriz) == contador:
                n_aux += 1
                parada3 += 1

    indireto = [None]*len(matriz)
    for pos in range(len(vetor)):
        if(vetor[pos] == 0):
            indireto[pos] = None
        elif(vetor[pos] == -1):
            indireto[pos] = 0
        else:
            indireto[pos] = vetor[pos].astype(np.int64)

    return indireto


def verificaGrafoConexo(matriz):
    print("Bem vindo ao verificador de Grafo Conexo!\n")

    try:
        verticeInicio = int(input("""Digite um vértice para iniciar
Escolha: """))  # -1 Para trabalhar com ínico 0 no código, e 1 pelo usuário.

        # Verifica se a matriz possui o vértice escolhido.
        if(verticeInicio > len(matriz) or verticeInicio <= 0):
            erro.mensagem()
            verificaGrafoConexo(matriz)
        else:
            buscaFechosTransitivos(matriz, verticeInicio - 1)

    except ValueError:
        os.system('pause')
        erro.mensagem()
        return verificaGrafoConexo(matriz)
