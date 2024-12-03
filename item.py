from abc import ABC, abstractmethod


class Item(ABC):

    def __init__(self, nome, preco):
        try:
            if not isinstance(nome, str):
                raise TypeError
            if not isinstance(preco, int):
                raise TypeError
            self.__nome = nome
            self.__preco = preco
        
        except TypeError:
            print("Houve um erro ao instanciar o item.")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        try:
            if not isinstance(nome, str):
                raise TypeError
            self.__nome = nome

        except TypeError:
            print("Houve um erro ao mudar o nome do item.")

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        try:
            if not isinstance(preco, int):
                raise TypeError
            self.__preco = preco

        except TypeError:
            print("Houve um erro ao mudar o preco do item.")
