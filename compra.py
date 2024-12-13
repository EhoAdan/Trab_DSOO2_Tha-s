from item import Item
from jogador import Jogador
from datetime import datetime

class Compra:

    def __init__(self, jogador: Jogador, item: Item, tipo_item: str, tipo_compra: str, num_compra: int):
        self.__jogador = jogador
        self.__item = item
        self.__data = datetime.today().strftime("%d/%m/%Y")
        self.__hora = datetime.now().strftime("%H:%M")
        self.__tipo_item = tipo_item
        self.__tipo_compra = tipo_compra
        self.__num_compra = num_compra
    
    @property
    def item(self):
        return self.__item
    
    @property
    def data(self):
        return self.__data

    @property
    def jogador(self):
        return self.__jogador

    @property
    def tipo_item(self):
        return self.__tipo_item

    @property
    def hora(self):
        return self.__hora

    @property
    def tipo_compra(self):
        return self.__tipo_compra

    @property
    def num_compra(self):
        return self.__num_compra