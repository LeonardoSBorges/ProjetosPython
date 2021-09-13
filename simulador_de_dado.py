#Simulador de dado
#Simular o uso de um dado, gerando um valor de 1 até 6


import random #gerar um numero aleatorio
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #layout
        self.layoutDado= [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        #janela
        self.janela = sg.Window('Simulado de Dado',layout=self.layoutDado)
        #ler os valores da tela
        self.eventos, self.valores = self.janela.Read()

        try:
            if self.eventos == 'Sim':
                self.GerarValorDoDado()
            elif self.eventos == 'Não':
                print('Agradecemos a sua participação')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        #gerar numeros inteiros
        print(random.randint(self.valor_minimo,self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()