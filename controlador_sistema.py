from tela_sistema import TelaSistema
from controlador_jogador import ControladorJogador
from controlador_loja import ControladorLoja
from jogador import Jogador

class ControladorSistema:
    __instance = None
    def __init__(self):
        self.__controlador_jogador = ControladorJogador(self)
        self.__loja = ControladorLoja(None, self)
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
        self.__tela_sistema.exibe_mensagem("Jogo encerrado.")
        exit()

    def login(self):
        while True:
            email_ou_usuario, senha_informada = self.__tela_sistema.login()
            usuario_existe = False
            if email_ou_usuario == '':  
                # Sai do login caso o botão cancelar seja apertado, também
                # sai do login caso confirme sem nada escrito, mas não sei bem como arrumar
                # de qualquer jeito, acho que não tem muito problema deixar assim
                break
            for usuario_registrado in self.__controlador_jogador.jogadores:
                if (usuario_registrado.email == email_ou_usuario or
                        usuario_registrado.nome == email_ou_usuario):
                    usuario_existe = True
                    if usuario_registrado.senha == senha_informada:
                        self.__controlador_jogador.jogador_logado = usuario_registrado
                        self.__loja.jogador = usuario_registrado
                        self.__logou = True
                        self.__tela_sistema.exibe_mensagem(f"Você logou como: {self.__controlador_jogador.jogador_logado.nome}")
                        return usuario_registrado
                    break # Sai do loop caso o usuário exista mas a senha esteja errada
            if not usuario_existe:
                self.__tela_sistema.exibe_mensagem("Usuário ou email não encontrado.")
            else:
                self.__tela_sistema.exibe_mensagem("Senha incorreta.")

    def criar_conta(self):
        conta_criada = False # Usado para verificar se saiu da tela de criar conta
                             # Criando uma conta ou só cancelando o processo
        while True:
            try:
                #Funciona
                nome, email, senha = self.__tela_sistema.criar_conta()
                if nome == '':
                    break
                if any(usuario_existe.nome == nome for usuario_existe 
                       in self.__controlador_jogador.jogadores):
                    mensagem = "Nome de usuário já existe."
                    raise NameError
                # Daqui até o break só é necessário por eu não ter conseguido implementar
                # botão desabilitado dinâmico, mas se decidirmos manter assim, dá pra criar
                # um erro customizado pra isso
                if len(senha) < 8:
                    mensagem = "Senha curta demais"
                    raise NameError
                if not any(char.isdigit() for char in senha):
                    mensagem = "Senha necessita de números"
                    raise NameError
                if not any(char.isalpha() for char in senha):
                    mensagem = "Senha necessita de letras"
                    raise NameError
                if not any(char == '@' for char in email) or email[0] == '@' or email[-1] == '@':
                    mensagem = "Email inválido"
                    raise NameError
                conta_criada = True
                break
            except NameError:
                self.__tela_sistema.exibe_mensagem(mensagem)
        if conta_criada:
            jogador_novo = Jogador(nome, email, senha)
            self.__controlador_jogador.jogadores.append(jogador_novo)
            self.__tela_sistema.exibe_mensagem(f"""Nova conta criada com sucesso!
Seu nome de Jogador é: {nome}
Seu e-mail é: {email}""")

    def abre_jogador(self):
        if not self.__logou:
            self.__tela_sistema.exibe_mensagem("Você precisa fazer login antes de jogar.")
            return None
        # Ações login não é um nome muito apropriado pra agora mas enfim
        self.__controlador_jogador.acoes_login()

    def abre_loja(self):
        if not self.__logou:
            self.__tela_sistema.exibe_mensagem("Você precisa fazer login antes de entrar na loja.")
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
# Talvez dê pra fazer um controlador só de login e criação de contas
