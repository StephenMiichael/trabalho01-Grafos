### Autores
# Lucas Stofella da silva
# Stephen Michael Apolinário
# Wesley Grignani
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
         4 - Busca em largura
         5 - Busca em profundidade
         6 - Voltar ao menu principal ( ⚠️ ⚠️  IRÁ EXCLUIR SEU GRAFO ⚠️ ⚠️  )
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
            os.system('cls')
        elif escolha == 4:
            os.system('cls')
            funcoes.buscaLargura(matriz)
        elif escolha == 5:
            os.system('cls')
            funcoes.buscaProfundidade(matriz)
        elif escolha == 6:
            os.system('cls')
            main()
        else:
            funcoes.erro()
            opcoesGrafo(matriz)
    except ValueError:
        funcoes.erro()
        opcoesGrafo(matriz)
    

def criacaoGrafo():
    try:
        vertices = int(input('Informe a quantidade de vertices do grafo: '))
        if(vertices <= 0):
            funcoes.erro()
            criacaoGrafo()
    except ValueError:
        funcoes.erro()
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
        1 - Lucas Stofella da silva
        2 - Stephen Michael Apolinário
        3 - Wesley Grignani

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
            funcoes.erro()
            main()
    except ValueError:
        funcoes.erro()
        main()

if __name__ == "__main__":
    os.system('cls')
    main()