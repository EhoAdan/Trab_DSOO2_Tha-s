from item import Item
from personagem import Personagem


class Skin(Item):

    def __init__(self, nome, preco, personagem):
        try:
            if not isinstance(personagem, Personagem):
                raise TypeError
            super().__init__(nome, preco)
            self.__personagem = personagem

        except TypeError:
            print("Houve um erro ao instanciar a skin.")

    @property
    def personagem(self):
        return self.__personagem

    @personagem.setter
    def personagem(self, personagem):
        try:
            if not isinstance(personagem, Personagem):
                raise TypeError
            self.__personagem = personagem

        except TypeError:
            print("Houve um erro ao modificar o personagem da skin.")
