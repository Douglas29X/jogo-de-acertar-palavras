from os import system
from jogo_de_adivinhacao import joga

def inicia():
    system('cls')
    print('''Boas vindas ao jogo de adivinhação de palavras!

***REGRAS***

Para começar, será mostrado na tela uma palavra embaralhada
(anagrama). A partir do momento em que você iniciar
o jogo, você terá que digitar ela na ordem correta. 

A partida durará 5 rodadas, sendo que a cada palavra acertada 
você ganha 1 ponto e, se caso for errada, perde 1 ponto.''')

    escolha = input(
        '\n\nEntão vamos lá! Para começar a jogar, aperte ENTER\n')

    if escolha == '':
        joga()
    else:
        print('Programa encerrado.')

if __name__ == '__main__':
    inicia()