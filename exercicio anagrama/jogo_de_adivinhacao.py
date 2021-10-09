from os import system
from palavra import Palavra

lista_palavras = []

def verifica_existencia(instancia):

    if instancia.palavra in lista_palavras:
        teste = Palavra()
        verifica_existencia(teste)
    else:
        teste = instancia

    lista_palavras.append(teste.palavra)
    return teste

def joga():
    system('cls')
    tentativas = 1
    pontos = 0

    while tentativas <= 5:
        print('*******************************\n\nJogando...\n\n')

        teste = Palavra()
        palavra = verifica_existencia(teste)

        print(f'O anagrama da vez é:\n{palavra.embaralha_letras()}\n')

        deducao = input('Digite a palavra correta:\n').upper()

        if deducao == palavra.palavra:
            print(f'\nParabéns, você acertou! A palavra era: {palavra}\n\n')
            pontos+=1
        else:
            print(f'\nQue pena, você errou. A palavra era {palavra}\n\n')
            if pontos > 0:
                pontos-=1
        
        tentativas+=1

    print(f'Jogo finalizado! Sua pontuação final é de {pontos} pontos.')