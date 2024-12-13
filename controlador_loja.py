from jogador import Jogador
from personagem import Personagem
from skin import Skin
from tela_loja import TelaLoja
from controlador_jogador import ControladorJogador
from compra import Compra
from loja_dao import LojaDAO


class ControladorLoja:

    def __init__(self, jogador: Jogador, controlador_sistema, historico_compras = []):
        # Serve como o controlador de itens
        self.__tela_loja = TelaLoja()
        self.__controlador_jogador = ControladorJogador(controlador_sistema)
        self.__jogador = jogador
        self.__jogador_logado = 0
        self.__historico_compras = historico_compras
        self.__loja_DAO = LojaDAO()
        self.__itens = [item for item in self.__loja_DAO.get_all()]

    @property
    def jogador(self):
        return self.__jogador

    @property
    def itens(self):
        return self.__itens

    @property
    def tela_loja(self):
        return self.__tela_loja

    @property
    def jogador_logado(self):
        return self.__jogador_logado

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    @property
    def loja_DAO(self):
        return self.__loja_DAO

    @jogador.setter
    def jogador(self, jogador):
        try:
            if not isinstance(jogador, Jogador):
                raise TypeError
            self.__jogador = jogador

        except TypeError:
            print("Houve um erro ao modificar o jogador.")

    @itens.setter
    def itens(self, itens):
        try:
            if not isinstance(itens, list):
                raise TypeError
            for objeto in itens:
                if not isinstance(objeto, Personagem) and not isinstance(objeto, Skin):
                    raise TypeError
            self.__itens = itens

        except TypeError:
            print("Houve um erro ao modificar a lista de itens da loja.")

    @tela_loja.setter
    def tela_loja(self, tela_loja):
        try:
            if not isinstance(tela_loja, TelaLoja):
                raise TypeError
            self.__tela_loja = tela_loja

        except TypeError:
            print("Houve um erro ao modificar a tela da loja.")

    @jogador_logado.setter
    def jogador_logado(self, jogador_logado):
        self.__jogador_logado = jogador_logado

    @controlador_jogador.setter
    def controlador_jogador(self, controlador_jogador):
        self.__controlador_jogador = controlador_jogador

    @property
    def historico_compras(self):
        return self.__historico_compras

    @historico_compras.setter
    def historico_compras(self, historico_compras):
        self.__historico_compras = historico_compras

    @loja_DAO.setter
    def loja_DAO(self, loja_DAO):
        self.__loja_DAO = loja_DAO

    def abre_tela(self):
        opcoes_loja = {0: None,
                1: self.buscar_todos_itens_loja,
                2: self.buscar_itens_disponiveis,
                3: self.comprar_item,
                4: self.ver_hist_compras,
                5: self.ver_hist_compras_proprio
                }

        while True:
            opcao = opcoes_loja[self.__tela_loja.menu_opcoes()]
            if not opcao:
                return None
            opcao()

    def buscar_todos_itens_loja(self):
        i = 0
        lista_itens = []
        for item in self.__itens:
            i += 1
            lista_itens.append(f"{i}: {item.nome}")
        self.__tela_loja.exibir_itens(lista_itens)
        return None

    def buscar_itens_disponiveis(self):
        i = 0
        lista_itens = []
        for item in self.__itens:
            if (item not in self.__jogador.lista_itens_jogador and
                (isinstance(item, Personagem) or item.personagem in self.__jogador.lista_itens_jogador)):
                # Basicamente, verifica se o item tá na lista de itens do jogador,
                # caso não esteja, verifica se é um personagem ou skin, caso seja skin,
                # verifica se o jogador tem o personagem ao qual a skin pertence
                i += 1
                lista_itens.append(f"{i}: {item.nome}")
        self.__tela_loja.exibir_itens(lista_itens)

    def comprar_item(self):
        # Vou deixar sem presentear por enquanto, mas se puxar do controlador de jogador
        # Deve dar sem muito problema
        while True:
            saldo = self.__jogador.saldo
            # Verifica se o item tá no inventário e adiciona ele caso seja um personagem ou,
            # caso seja uma skin, o personagem à qual a skin pertence tá no inventário
            itens_disponiveis = [item for item in self.__itens if item 
                                 not in self.__jogador.lista_itens_jogador and 
                                 (isinstance(item, Personagem) or item.personagem in 
                                  self.__jogador.lista_itens_jogador)]
            amigos = self.__jogador.amigos
            item_comprado = self.__tela_loja.comprar_item(saldo, itens_disponiveis, amigos)
            if item_comprado == 0:  # Caso seja cancelada a compra
                return None
            item_comprado = itens_disponiveis[item_comprado - 1] # Pega o número retornado e vê qual item
                                                                 # tá na posição
            if not item_comprado:
                return None
            if saldo >= item_comprado.preco:
                if isinstance(item_comprado, Skin):
                    tipo_item = "skin"
                else:
                    tipo_item = "personagem"
                compra = Compra(self.__jogador, item_comprado, tipo_item)
                self.__jogador.saldo -= item_comprado.preco
                self.__jogador.lista_itens_jogador.append(item_comprado)
                self.__historico_compras.append(compra)
                self.__tela_loja.exibe_mensagem(f"Sucesso, você comprou {item_comprado.nome} por {item_comprado.preco}!")
                return None
            self.__tela_loja.exibe_mensagem("Saldo insuficiente.")

    def ver_hist_compras(self):
        hist_compras = []
        for compra in self.__historico_compras:
            hist_compras.append(f"{compra.jogador.nome} comprou o/a {compra.tipo_item} "
                                f"{compra.item.nome} por {compra.item.preco} pontos no dia {compra.data} "
                                f"às {compra.hora}.")
        self.__tela_loja.historico_compras(hist_compras)
        return None

    def ver_hist_compras_proprio(self):
        hist_compras = []
        for compra in self.__historico_compras:
            if compra.jogador.nome == self.__jogador.nome:
                hist_compras.append(f"{compra.jogador.nome} comprou o/a {compra.tipo_item} "
                                f"{compra.item.nome} por {compra.item.preco} pontos no dia {compra.data} "
                                f"às {compra.hora}.")
        self.__tela_loja.historico_compras(hist_compras)
        return None
