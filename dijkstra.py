# Autores
# Lucas Stofella da silva
# Stephen Michael Apolinário
# Wesley Grignani
import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import numpy as np  # Para manipulação de matrizes
import erro  # Para mostrar mensagens de erro
import main  # Para voltar ao script principal

# Definir custo entre as ligações


def matriz_de_custo(matriz):
    # Matriz Exemplo Slide Dijkstra
    matriz[0][1] = 2
    matriz[0][3] = 1
    matriz[1][3] = 3
    matriz[1][4] = 10
    matriz[2][0] = 4
    matriz[2][5] = 5
    matriz[3][2] = 2
    matriz[3][4] = 2
    matriz[3][5] = 8
    matriz[3][6] = 4
    matriz[4][6] = 6
    matriz[6][5] = 1

    while True:
        os.system('cls')
        try:
            escolha = int(input("""Opções de arestas:
         1 - Incluir arestas com custo
         2 - Excluir arestas com custo
         3 - Calcular Menor Caminho
         4 - Voltar ao menu principal
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
                        custo = int(input('Custo: '))
                        if(custo <= 0):
                            erro.mensagem()
                            break
                        matriz[v1-1][v2-1] = custo
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
                        matriz_de_custo(matriz)

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
                        matriz_de_custo(matriz)

            elif escolha == 3:
                os.system('cls')
                return matriz

            elif escolha == 4:
                os.system('cls')
                return main.opcoesGrafo(matriz)

            else:
                erro.mensagem()
        except ValueError:
            erro.mensagem()
            matriz_de_custo(matriz)


def menor_caminho(matriz):

    visitados = np.zeros(len(matriz), dtype=np.float64)
    estimativas = 500 * np.ones(len(matriz), dtype=np.float64)
    precedentes = np.zeros(len(matriz), dtype=np.float64)

    matriz = matriz_de_custo(matriz)

    origem = int(input('Informe o vertice de origem: '))
    origem -= 1
    visitados[origem] = 1
    estimativas[origem] = 500
    precedentes[origem] = origem

    parada = 0
    valor = 0

    while parada == 0:

        for x in range(len(matriz)):
            if matriz[origem][x] != 0 and visitados[x] == 0:
                if matriz[origem][x] + valor < estimativas[x]:
                    estimativas[x] = matriz[origem][x] + valor
                    precedentes[x] = origem

        if visitados.mean() == 1:
            parada = 1

        iMenor = 0

        for j in range(len(matriz)):
            if estimativas[j] == 0:
                pass
            elif estimativas[j] < estimativas[iMenor] and visitados[j] == 0:
                iMenor = j

        origem = iMenor
        visitados[iMenor] = 1
        valor = estimativas[iMenor]

    for k in range(len(matriz)):
        if estimativas[k] == 500:
            estimativas[k] = 0

    print('Resultado: \n')
    print(estimativas)
    print('Pressione ESC para voltar ao menu principal.')
    keyboard.wait('esc')
    os.system('cls')
    main.opcoesGrafo(matriz)
