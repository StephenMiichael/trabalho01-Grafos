# pip3 install keyboard
# Fazer um programa que permita a inclusão de um grafo (dirigido ou não dirigido), mostrando o Grafo (desenhado) ou a Matriz/lista de adjacências.
# O programa deve permitir:
# - Incluir ou excluir vértices e arestas/arcos a qualquer tempo
# - Fazer busca em Largura e Profundidade. Com opção de buscar algum elemento do grafo ou mostrar todos os vértices do grafo na ordem de visitação.
# - O ponto de inicio da busca deve ser informado pelo usuário.

# --> Trabalho pode ser feito em duplas.

# --> Atenção ao prazo para publicação da solução.
import os #Para limpar o terminal.
import keyboard #Para escutar as teclas pressionadas

def criacaoGrafo():
    os.system('cls')
    print("""Trabalho em construção!! Por favor, volte mais tarde xD

Para voltar ao menu, tecle esc!
          """)
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
    print('Bem vindo ao trabalho 01\n');
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
        print("Este número não está nas alternativas, tente novamente :D.\n")
        main()

if __name__== "__main__" :
    main()
