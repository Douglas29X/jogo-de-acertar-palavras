import random

class Palavra:
    def __init__(self):
        self.__palavra = self.gera_nova_palavra()

    def gera_nova_palavra(self):
        with open('lista_de_palavras.csv', 'r') as arquivo:
            palavras = []
            for palavra in arquivo:
                palavra = palavra.strip().upper()
                palavras.append(palavra)
            numero = random.randint(0,len(palavras) - 1)
            return palavras[numero]

    def embaralha_letras(self):
        anagrama = ''
        letra = random.sample(self.__palavra, len(self.__palavra))
        anagrama+= anagrama.join(letra)
        return anagrama.upper()
    
    def __str__(self):
        return self.__palavra
    
    @property
    def palavra(self):
        return self.__palavra