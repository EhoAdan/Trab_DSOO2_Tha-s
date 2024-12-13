rom tela_jogador import TelaJogador
from item import Item
from jogador import Jogador
from alteracao_exception import AlteracaoException
from personagem import Personagem
from skin import Skin
#Personagem e Skins estão aqui apenas
#Para facilitar a apresentação

class ControladorJogador:

    def __init__(self, controlador_sistema):
        self.__jogadores = [Amale, Tchali, B_de_Bingança, Teste]
        self.__tela_jogador = TelaJogador()
        self.__controlador_sistema = controlador_sistema
        self.__jogador_logado = False

    @property
    def jogador_logado(self):
        return self.__jogador_logado

    @property
    def jogadores(self):
        return self.__jogadores

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @jogadores.setter
    def jogadores(self, jogadores):
        self.__jogadores = jogadores

    @jogador_logado.setter
    def jogador_logado(self, jogador_logado):
        self.__jogador_logado = jogador_logado

    def abre_tela(self):
        opcoes_tela = {0: None,
                1: self.listar, #Mexer daqui pra frente
                2: self.estats,
                3: self.alterar,
                4: self.deletar}
        
        while True:
            opcao = opcoes_tela[self.__tela_jogador.abre_tela()]
            if not opcao:
                return None
            opcao()

    def acoes_login(self):
        opcoes_jogador = {0: None,
                1: self.abre_tela,
                2: self.jogar_partida,
                3: self.historico_partidas,
                4: self.adicionar_amigo,
                5: self.excluir_amigo,
                6: self.listar_amigos
                }
        
        while True:
            opcao = opcoes_jogador[self.__tela_jogador.acoes_login()]
            if not opcao:
                return None
            opcao()

    def jogar_partida(self):
        self.__jogador_logado.partidas_jogadas += 1
        self.__tela_jogador.jogar_partida(self.__jogador_logado.partidas_jogadas)

    def historico_partidas(self):
        self.__tela_jogador.mostra_partidas_jogadas(self.__jogador_logado.partidas_jogadas)

    def eh_jogador(self, nome_jogador):
        for jogador_existe in self.__jogadores:
            if jogador_existe.nome == nome_jogador:
                return jogador_existe
        return None

    def adicionar_amigo(self):
        nome_jogador = input("Digite o nome do jogador que quer adicionar: ")
        jogador_existe = self.eh_jogador(nome_jogador)
        if not isinstance(jogador_existe, Jogador):
            print("Houve uma tentativa de adicionar um não-jogador como amigo.")
        elif jogador_existe.nome == self.__jogador_logado.nome:
            print("Você não pode se adicionar como amigo.")
        elif any(jogador_existe.nome == amigo.nome for amigo in self.__jogador_logado.amigos):
            print(f"{jogador_existe.nome} já é seu amigo.")
        else:
            self.__jogador_logado.amigos.append(jogador_existe)
            print(f"{jogador_existe.nome} adicionado com sucesso à sua lista de amigos.")

    def excluir_amigo(self):
        nome_jogador = input("Digite o nome do amigo que quer excluir: ")
        jogador_existe = self.eh_jogador(nome_jogador)
        for amigo in self.__jogador_logado.amigos:
            if jogador_existe.nome == amigo.nome:
                self.__jogador_logado.amigos.remove(amigo)

    def listar_amigos(self):
        amigos = []
        if len(self.__jogador_logado.amigos) > 0:
            for amigo in self.__jogador_logado.amigos:
                amigos.append(amigo.nome)
            self.__tela_jogador.lista_amigos(amigos)
        else:
            self.__tela_jogador.lista_amigos_zero()
        
    def listar(self): #Interface Gráfica feita
        lista_jogadores = []
        for jogador in self.__jogadores:
            lista_jogadores.append(jogador.nome)

        self.__tela_jogador.mostra_lista_jogadores(lista_jogadores)

    def estats(self):
        mais_dinheiro_gasto = 0
        mais_presentes_dados = 0
        mais_partidas_jogadas = 0
        mais_itens = 0
        jog_mais_dinheiro_gasto = None
        jog_mais_presenteador = None
        jog_mais_partidas = None
        jog_mais_itens = None
        for jogador in self.__jogadores:
            if jogador.dinheiro_gasto > mais_dinheiro_gasto:
                jog_mais_dinheiro_gasto = jogador
                mais_dinheiro_gasto = jogador.dinheiro_gasto
            if jogador.presentes_dados > mais_presentes_dados:
                jog_mais_presenteador = jogador
                mais_presentes_dados = jogador.presentes_dados
            if jogador.partidas_jogadas > mais_partidas_jogadas:
                jog_mais_partidas = jogador
                mais_partidas_jogadas = jogador.partidas_jogadas
            if len(jogador.lista_itens_jogador) > mais_itens:
                jog_mais_itens = jogador
                mais_itens = len(jogador.lista_itens_jogador)
        
        self.__tela_jogador.tela_estats(mais_dinheiro_gasto, mais_presentes_dados, \
                                mais_partidas_jogadas, mais_itens, \
                                jog_mais_dinheiro_gasto, jog_mais_presenteador, \
                                jog_mais_partidas, jog_mais_itens)

    
    def alterar(self):
        email_informado = input("Favor, confirme seu endereço de e-mail: ")
        senha_informada = input("Favor, confirme sua senha: ")
        for usuario_registrado in self.__jogadores:
            if usuario_registrado.email == email_informado:
                if usuario_registrado.senha == senha_informada:
                    novo_nome = input("Favor, digite seu novo nome: ")
                    if any(usuario_registrado.nome == novo_nome for usuario_registrado in self.__jogadores):
                        print("Nome de usuário já existe")
                        raise AlteracaoException
                    else:
                        usuario_registrado.nome = novo_nome
                        print(f"""Nome alterado com sucesso!
Seu novo nome é: {usuario_registrado.nome}""")
                    return None
                break


    def deletar(self):
        email_informado = input("Favor, confirme seu endereço de e-mail: ")
        senha_informada = input("Favor, confirme sua senha: ")
        try:
            for usuario_registrado in self.__jogadores:
                if usuario_registrado.email == email_informado:
                    if usuario_registrado.senha == senha_informada:
                        print("""Excluir uma conta é um processo permanente!
Tem certeza que deseja excluí-la?
0- Não, não desejo excluir minha conta.
9- Sim, desejo excluir minha conta.
""")
                        resposta = int(input())
                        if resposta == 9:
                            self.__jogadores.remove(usuario_registrado)
                            print("""Conta excluída com sucesso!
Retornando à tela anterior.""")
                            self.__controlador_sistema.abre_tela()
                        elif resposta == 0:
                            print("Que bom que decidiu não excluir sua conta e continuar conosco!")
                            self.abre_tela()
                        else:
                            print("Opção inválida! Retornando a tela anterior.")
                            self.abre_tela()
        except ValueError:
            print("Opção inválida! Retornando a tela anterior.")
            return self.abre_tela()

#Lista preliminar de jogadores e itens

ornn = Personagem("Ornn", 1000, ["Ornn Florescer Espiritual"])
ornn_flor_esp = Skin("Ornn Florescer Espiritual", 500, ornn)
mordekaiser = Personagem("Mordekaiser", 800)
kratos = Personagem("Kratos", 500, ["Kratos Nórdico"])
kratos_nordico = Skin("Kratos Nórdico", 200, kratos)
pikachu = Personagem("Pikachu", 52, ["Pikachu Surfista", "Pikachu-Ash", "Pikachu Luta-Libre", "Pikachu Gigantamax"])
pikachu_surf = Skin("Pikachu Surfista", 2, pikachu)
pikachu_ash = Skin("Pikachu Ash", 22, pikachu)
pikachu_wwe = Skin("Pikachu Luta-Libre", 30, pikachu)
pikachu_gmax = Skin("Pikachu Gigantamax", 1200, pikachu)

Amale = Jogador("Amale", "amale@gmail.com", "amale123", 150, \
                [ornn, ornn_flor_esp, mordekaiser, kratos, kratos_nordico, \
                 pikachu, pikachu_ash, pikachu_gmax, pikachu_surf, pikachu_wwe], \
                    50000, 13, 7, 596)
Tchali = Jogador("Tchali", "tchali123@gmail.com.br", "tchali123", 260, \
                 [ornn, ornn_flor_esp, mordekaiser, kratos, kratos_nordico], \
                 42000, 26, 18, 126)
B_de_Bingança = Jogador("B de Bingança", "B@B", "123", 3000, \
                        [pikachu, pikachu_ash, pikachu_gmax, pikachu_surf, pikachu_wwe], \
                        36000, 0, 1, 5612)
Teste = Jogador("Teste", "a", "a", 10000)
