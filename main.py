# pip3 install keyboard
# Fazer um programa que permita a inclusão de um grafo (dirigido ou não dirigido), mostrando o Grafo (desenhado) ou a Matriz/lista de adjacências.
# O programa deve permitir:
# - Incluir ou excluir vértices e arestas/arcos a qualquer tempo
# - Fazer busca em Largura e Profundidade. Com opção de buscar algum elemento do grafo ou mostrar todos os vértices do grafo na ordem de visitação.
# - O ponto de inicio da busca deve ser informado pelo usuário.

# --> Trabalho pode ser feito em duplas.

# --> Atenção ao prazo para publicação da solução.
import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import numpy as np
import funcoes

def criacaoGrafo():
    os.system('cls')
    vertices = int(input('Informe a quantidade de vertices do grafo: '))
    matriz = np.zeros((vertices, vertices), dtype=np.float64)

    while True:
        os.system('cls')
        escolha = int(input("""Grafo Criado 
              1 - Incluir ou Excluir arestas/arcos
              2 - Incluir ou Excluir vertices 
              3 - Imprimir matriz de adjacencias
              4 - Sair 
              
              Escolha: """))

        if escolha == 1:
            matriz = funcoes.arestas(matriz)
        elif escolha == 2:
            matriz = funcoes.vertices(matriz)
        elif escolha == 3:
            print(matriz)
            keyboard.wait('esc')
        elif escolha == 4:
            break
        else:
            os.system('cls')
            print("Este número não está nas alternativas, tente novamente :D.\n")

    print('Voltando para o menu inicial !!')
    keyboard.wait('esc')
    os.system('cls')
    main()

def sair():
    exit()

def creditos():
    print("""Acadêmicos:
        1 - Stephen Micahel Apolinário
        2 - Wesley Grignani
        3 - Lucas Stofella

    Para voltar ao menu, tecle esc!
         """)
    keyboard.wait('esc')
    os.system('cls')
    main()

def main():
    print('Bem vindo ao trabalho 01\n')
    try:
        opcao = int(input("""Selecione uma opção: 
                1 - Entrar no programa
                2 - Créditos
                3 - Sair

    Escolha:  """))
        if opcao == 1:
            criacaoGrafo()
        elif opcao == 2:
            os.system('cls')
            print('###CRÉDITOS###')
            creditos()
        elif opcao == 3:
            sair()
        else:
            os.system('cls')
            print("Este número não está nas alternativas, tente novamente :D.\n")
            main()
    except ValueError:
        os.system('cls')
        print("Isso não é um número, tente novamente :D.\n")
        main()

if __name__ == "__main__":
    os.system('cls')
    main()