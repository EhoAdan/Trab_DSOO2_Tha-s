import PySimpleGUI as sg

class TelaLoja():
    def __init__(self):
        self.__window = None
        self.init_components()
    
    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('NeonYellow1')
        layout = [
            [sg.Text('Loja de Itens', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Buscar todos os itens da loja',"RD1", key='1')],
            [sg.Radio('Buscar os itens disponíveis',"RD1", key='2')],
            [sg.Radio('Comprar um item',"RD1", key='3')],
            [sg.Radio('Ver o histórico de compras geral',"RD1", key='4')],
            [sg.Radio('Ver o seu histórico de compras',"RD1", key='5')],
            [sg.Radio('Retornar', 'RD1', key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('O jogo').Layout(layout)

    def menu_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def exibir_itens(self, lista_itens):
        layout = [
            [sg.Text("Itens", font=("Helvica", 25))],
            [[sg.Text(item)] for item in lista_itens],
            [sg.Button('Ok')]
        ]
        self.__window = sg.Window('Loja').Layout(layout)
        self.__window.Read()
        self.close()

    def comprar_item(self, saldo, lista_itens, amigos_jogador):
        # Adiciono items para compra conforme quais itens estão disponíveis por list comprehension
        layout = [
            [sg.Text('Selecione qual item comprar', font=("Helvica",25))],
            [sg.Text(f'Seu saldo é de {saldo} pontos.', font=("Helvica",15))],
            [[sg.Radio(f'{item.nome} por {item.preco}', "RD1", 
                       key=str(lista_itens.index(item) + 1))] for item in lista_itens],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Loja').Layout(layout)
        button, values = self.__window.Read()
        opcao = 0
        if button in (None, 'Cancelar'):
            opcao = 0
        else: # Testa as opções
            for i in range(1, len(lista_itens) + 1):
                if values[str(i)]:
                    opcao = i
                    break
        self.close()
        return opcao

    def historico_compras(self, hist_compras):
        layout = [
            [[sg.Text(compra)] for compra in hist_compras],
            [sg.Button('Ok')]
        ]
        self.__window = sg.Window('Loja').Layout(layout)
        self.__window.Read()
        self.close()

    def exibe_mensagem(self, mensagem):
        layout = [
            [sg.Text(mensagem)],
            [sg.Button('Ok')]
        ]
        self.__window = sg.Window('Loja').Layout(layout)
        self.__window.Read()
        self.close()