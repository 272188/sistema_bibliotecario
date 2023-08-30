from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import socket
import sys

from modelos import Usuario, Livro, Emprestimo

from telas.tela_login import Ui_Login
from telas.tela_cadastro import Ui_Cadastro
from telas.tela_livro import Ui_Livro
from telas.tela_admin import Ui_Admin
from telas.tela_principal import Ui_Principal
# pyuic5 -x designer/tela_principal.ui -o tela_principal.py


ip = host = socket.gethostbyname(socket.gethostname())
# ip = '10.180.44.205'
port = 8080
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(addr)
except:
    print("\nNao foi possivel se conectar ao servidor!\n")
    exit()

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()

        self.tela_login = Ui_Login()
        self.tela_login.setupUi(self.stack0)
        self.tela_pricipal = Ui_Principal()
        self.tela_pricipal.setupUi(self.stack1)
        self.tela_admin = Ui_Admin()
        self.tela_admin.setupUi(self.stack2)
        self.tela_cadastro = Ui_Cadastro()
        self.tela_cadastro.setupUi(self.stack3)
        self.tela_livro = Ui_Livro()
        self.tela_livro.setupUi(self.stack4)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.tela_login.botao_login.clicked.connect(self.enviar_login)
        self.tela_login.botao_fechar.clicked.connect(self.botao_fechar)
        self.tela_pricipal.botao_sair.clicked.connect(self.botao_sair)

    def enviar_login(self):
        email = self.tela_login.caixa_email.text()
        senha = self.tela_login.caixa_senha.text()
        if email and senha:
            client_socket.send(f"2,{email},{senha}".encode())
            resposta = client_socket.recv(1024).decode().split('|')
            if resposta[0] == "2":
                for registro in resposta[1:-1]:
                    self.tela_pricipal.inserir(self.tela_pricipal.tabela_emprestimos, registro.split(',')[1:])
                self.QtStack.setCurrentIndex(1)
            else:
                QMessageBox.about(self, "Erro", "Email ou senha incorretos!")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos!")

    def botao_sair(self):
        client_socket.send("0".encode())
        self.tela_pricipal.limpar(self.tela_pricipal.tabela_emprestimos)
        self.tela_pricipal.limpar(self.tela_pricipal.tabela_livros)
        self.QtStack.setCurrentIndex(0)

    def botao_fechar(self):
        client_socket.send("-1".encode())
        client_socket.close()
        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())