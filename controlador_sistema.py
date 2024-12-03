from tela_sistema import TelaSistema

from controlador_jogador import ControladorJogador
from controlador_loja import ControladorLoja
from personagem import Personagem
from jogador import Jogador
from skin import Skin

class ControladorSistema:
    __instance = None
    def __init__(self, jogador, itens):
        self.__controlador_jogador = ControladorJogador(self)
        self.__loja = ControladorLoja(jogador, self, itens)
        self.__tela_sistema = TelaSistema()
        self.__logou = False

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    @property
    def loja(self):
        return self.__loja

    @property
    def logou(self):
        return self.__logou

    @property
    def jogador_logado(self):
        return self.__jogador_logado

    @jogador_logado.setter
    def jogador_logado(self, jogador_logado):
        self.__jogador_logado = jogador_logado
    
    @controlador_jogador.setter
    def controlador_jogador(self, controlador_jogador):
        self.__controlador_jogador = controlador_jogador
    
    @logou.setter
    def logou(self, logou):
        self.__logou = logou

    @loja.setter
    def loja(self, loja):
        self.__loja = loja

    def inicializa_sistema(self):
        self.abre_tela()

    def encerrar(self):
        print("Jogo encerrado")
        exit()

    def login(self):
        email_ou_usuario = input("Favor, digite seu endereço de e-mail ou usuário: ")
        senha_informada = input("Favor, digite sua senha: ")
        for usuario_registrado in self.__controlador_jogador.jogadores:
            if (usuario_registrado.email == email_ou_usuario or
                usuario_registrado.nome == email_ou_usuario):
                if usuario_registrado.senha == senha_informada:
                    self.__controlador_jogador.jogador_logado = usuario_registrado
                    self.__loja.jogador = usuario_registrado
                    self.__logou = True
                    print(f"Você logou como: {self.__controlador_jogador.jogador_logado.nome}")
                    return usuario_registrado
        print("Usuário, email ou senha estão errados.")
        return None

    def criar_conta(self):
        while True:
            # Caso não surja o NameError, ou seja, ter o email certo, quebra o loop
            try:
                #Funciona
                email = str(input("Digite seu endereço de e-mail: "))
                if any(email_usado.email == email for email_usado in 
                       self.__controlador_jogador.jogadores):
                    print("E-mail já está em uso")
                    raise NameError
                if ("@" not in email or email[0] == "@" or email[-1] == "@"):
                    raise NameError
                break
            except NameError:
                print("Favor inserir um e-mail válido")
        while True:
            try:
                #Funciona
                nome = str(input("Digite seu nome de usuário: "))
                if any(usuario_existe.nome == nome for usuario_existe 
                       in self.__controlador_jogador.jogadores):
                    print("Nome de usuário já existe")
                    raise NameError
                break
            except NameError:
                print("Favor inserir um nome válido")
        while True:
            try:
                #Funciona
                senha = input("""Digite sua senha
Ela deve possuir:
Ao menos 8 caracteres
Ao menos um número
Ao menos uma letra
""")
                if len(senha) < 8:
                    print("Senha muito curta!")
                    raise NameError
                if not any(caractere.isnumeric() for caractere in senha):
                    print("Senha não possui número!")
                    raise NameError
                if not any(caractere.isalpha() for caractere in senha):
                    print("Senha não possui letra!")
                    raise NameError
                break
            except NameError:
                print("Favor inserir uma senha válida")
        jogador_novo = Jogador(nome, email, senha)
        self.__controlador_jogador.jogadores.append(jogador_novo)
        print(f"""Nova conta criada com sucesso!
Seu nome de Jogador é: {nome}
Seu e-mail é: {email}
Sua senha é: {senha}
""")

    def abre_jogador(self):
        if not self.__logou:
            print("Você precisa realizar LogIn antes de Jogar")
            return None
        # Ações login não é um nome muito apropriado pra agora mas enfim
        self.__controlador_jogador.acoes_login()

    def abre_loja(self):
        if not self.__logou:
            print("Você precisa realizar LogIn antes de abrir a Loja")
            return None
        self.loja.abre_tela()

    def abre_tela(self):
        tela_opcoes = {0: self.encerrar,
                    1: self.abre_jogador,
                    2: self.abre_loja,
                    3: self.criar_conta,
                    4: self.login}
        while True:
            tela_opcoes[self.__tela_sistema.menu_opcoes()]()


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
itens = [ornn, ornn_flor_esp, mordekaiser, kratos, kratos_nordico, pikachu, pikachu_ash,
                    pikachu_gmax, pikachu_surf, pikachu_wwe]
ControladorSistema(None, itens).abre_tela()

