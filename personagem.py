from item import Item


class Personagem(Item):

    def __init__(self, nome, preco, lista_skins = []):
        try:
            super().__init__(nome, preco)
            if not isinstance(lista_skins, list) and lista_skins:
                raise TypeError
            for skin in lista_skins:
                # Pra evitar personagem e skin ser uma via de mão dupla, a lista vai ter
                # só o nome das skins
                if not isinstance(skin, str):
                    raise TypeError
            self.__lista_skins = lista_skins

        except TypeError:
            print("Houve um erro ao instanciar o personagem.")

    @property
    def lista_skins(self):
        return self.__lista_skins

    @lista_skins.setter
    def lista_skins(self, lista_skins):
        try:
            if not isinstance(lista_skins, list) or not lista_skins:
                raise TypeError
            self.__lista_skins = lista_skins

        except TypeError:
            print("Houve um erro ao modificar a lista de skins.")
