from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_janelaPrincipal as Ui_MainWindow
import random
import threading
import time
from datetime import datetime
import socket


class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        self.tela.bt_1.clicked.connect(self.clicado_1)      
        self.tela.bt_2.clicked.connect(self.clicado_2)
        
        self.tela.bt_3.clicked.connect(self.clicado_3)
        self.caixa, self.servidor = self.busca_dados()
    def busca_dados(self):
        arquivo = open("config.txt", 'r')
        dados=[]
        dados.append(arquivo.readline()[0:-1])
        dados.append(arquivo.readline())
        arquivo.close()
        return dados

    def clicado_1(self):
        self.preparar_mensagem(1)

    def clicado_2(self):
        self.preparar_mensagem(2)

    def clicado_3(self):
        self.preparar_mensagem(3)

    def preparar_mensagem(self, botao):
        mensagem = [botao, self.caixa, (self.tela.entrada_msg.toPlainText())]
        self.enviar_mensagem(mensagem)

    def enviar_mensagem(self, mensagem):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((socket.gethostbyname(self.servidor), 12397))
            self.s.send(str(mensagem).encode())
            self.tela.entrada_msg.setText("")
            self.s.close()
        except:
            self.s.close()
            print("ocorreu um erro")
