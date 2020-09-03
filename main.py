# pip3 install keyboard
# Fazer um programa que permita a inclusão de um grafo (dirigido ou não dirigido), mostrando o Grafo (desenhado) ou a Matriz/lista de adjacências.
# O programa deve permitir:
# - Incluir ou excluir vértices e arestas/arcos a qualquer tempo
# - Fazer busca em Largura e Profundidade. Com opção de buscar algum elemento do grafo ou mostrar todos os vértices do grafo na ordem de visitação.
# - O ponto de inicio da busca deve ser informado pelo usuário.

# --> Trabalho pode ser feito em duplas/trios.

# --> Atenção ao prazo para publicação da solução.
import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import numpy as np # Para manipulação de matrizes
import funcoes # Arquivo de funcoes

def opcoesGrafo(matriz):
    try:
        escolha = int(input("""Opções de grafo:
            1 - Incluir ou Excluir arestas/arcos
            2 - Incluir ou Excluir vertices 
            3 - Imprimir matriz de adjacencias
            4 - Voltar ao menu principal (⚠️ ⚠️  IRÁ EXCLUIR SEU GRAFO ⚠️ ⚠️ )
   Escolha: """))

        if escolha == 1:
            matriz = funcoes.arestas(matriz)
        elif escolha == 2:
            matriz = funcoes.vertices(matriz)
        elif escolha == 3:
            os.system('cls')
            print(f'{matriz}\n')
            print('Para voltar as opções, pressione ESC')
            keyboard.wait('esc')
        elif escolha == 4:
            os.system('cls')
            main()
        else:
            os.system('cls')
            print("Este número não está nas alternativas, tente novamente :D.\n")
            os.system('pause')
            os.system('cls')
            opcoesGrafo(matriz)
    except ValueError:
        os.system('cls')
        print("Isso não é um número, tente novamente :D.\n")
        os.system('pause')
        os.system('cls')
        opcoesGrafo(matriz)

def criacaoGrafo():
    try:
        vertices = int(input('Informe a quantidade de vertices do grafo: '))
        if(vertices <= 0):
            os.system('cls')
            print("Você digitou um menor ou igual a 0! Por favor, escolha um número positivo.\n")
            os.system('pause')
            os.system('cls')
            criacaoGrafo()
    except ValueError:
        os.system('cls')
        print("Isso não é um número, tente novamente :D.\n")
        os.system('pause')
        os.system('cls')
        criacaoGrafo()
    matriz = np.zeros((vertices, vertices), dtype=np.float64)

    while True:
        os.system('cls')
        print('Grafo Criado com sucesso\n')
        opcoesGrafo(matriz)

    os.system('cls')
    main()

def sair():
    exit()

def creditos():
    print("""Acadêmicos:
        1 - Stephen Micahel Apolinário
        2 - Wesley Grignani
        3 - Lucas Stofella

    Para voltar ao menu, pressione ESC!
         """)
    keyboard.wait('esc')
    os.system('cls')
    main()

def main():
    print('Bem vindo ao trabalho 01\n')
    try:
        opcao = int(input("""Selecione uma opção: 
                1 - Criar grafo
                2 - Créditos
                3 - Sair
       Escolha: """))
        if opcao == 1:
            os.system('cls')
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
            os.system('pause')
            os.system('cls')
            main()
    except ValueError:
        os.system('cls')
        print("Isso não é um número, tente novamente :D.\n")
        os.system('pause')
        os.system('cls')
        main()

if __name__ == "__main__":
    os.system('cls')
    main()