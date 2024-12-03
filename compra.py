from item import Item
from jogador import Jogador
from datetime import datetime

class Compra:

    def __init__(self, jogador: Jogador, item: Item, tipo_item: str):
        self.__jogador = jogador
        self.__item = item
        self.__data = datetime.today().strftime("%m-%Y")
        self.__tipo_item = tipo_item
    
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
