from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import socket
import sys
import datetime

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
        self.tela_pricipal.botao_devolver.clicked.connect(self.devolver_livro)
        self.tela_pricipal.botao_buscar.clicked.connect(self.buscar_livros)
        self.tela_pricipal.botao_emprestimo.clicked.connect(self.realizar_emprestimo)
        self.tela_pricipal.botao_sair.clicked.connect(self.botao_sair)
        self.tela_admin.botao_sair.clicked.connect(self.botao_sair)
    
    def atualizar_emprestimos(self):
        client_socket.send(f"6".encode())
        resposta = client_socket.recv(1024).decode().split('|')
        if resposta[0] == "6":
            self.tela_pricipal.limpar(self.tela_pricipal.tabela_emprestimos)
            for registro in resposta[1:-1]:
                self.tela_pricipal.inserir(self.tela_pricipal.tabela_emprestimos, registro.split(','))

    def buscar_livros(self):
        busca = self.tela_pricipal.caixa_buscar.text()
        if busca:
            client_socket.send(f"3,{busca}".encode())
            resposta = client_socket.recv(1024).decode().split('|')
            if resposta[0] == "3":
                self.tela_pricipal.limpar(self.tela_pricipal.tabela_livros)
                for registro in resposta[1:-1]:
                    registro = registro.split(',')
                    registro[-1] = 'Disponivel' if registro[-1] == '1' else 'Indisponivel'
                    self.tela_pricipal.inserir(self.tela_pricipal.tabela_livros, registro)
            else:
                QMessageBox.about(self, "Informe", "Nenhum livro encontrado!")
        else:
            QMessageBox.about(self, "Erro", "Preencha o campo de busca!")

    def realizar_emprestimo(self):
        id_livro = self.tela_pricipal.caixa_emprestimo.text()
        if linha := self.tela_pricipal.buscar(id_livro, self.tela_pricipal.tabela_livros):
            if self.tela_pricipal.tabela_livros.item(linha, 9).text() == 'Disponivel':
                client_socket.send(f"4,{id_livro}".encode())
                resposta = client_socket.recv(1024).decode()
                if resposta == "4":
                    QMessageBox.about(self, "Aviso", "Livro emprestado com sucesso!")
                    self.tela_pricipal.tabela_livros.item(linha, 9).setText('Indisponivel')
                    self.atualizar_emprestimos()
                else:
                    QMessageBox.about(self, "Erro", "Livro não encontrado!")
            else:
                QMessageBox.about(self, "Erro", "Livro indisponivel!")
        else:
            QMessageBox.about(self, "Erro", "Livro não encontrado!")

    def devolver_livro(self):
        id_livro = self.tela_pricipal.caixa_devolver.text()
        if linha := self.tela_pricipal.buscar(id_livro, self.tela_pricipal.tabela_emprestimos):
            client_socket.send(f"5,{id_livro}".encode())
            resposta = client_socket.recv(1024).decode()
            if resposta == "5":
                data_devolucao = self.tela_pricipal.tabela_emprestimos.item(linha, 10).text()
                atraso = datetime.datetime.now() - datetime.datetime.strptime(data_devolucao, "%Y-%m-%d")
                if atraso.days > 0:
                    QMessageBox.about(self, "Aviso", f"Livro devolvido com atraso! Multa de R$ {atraso.days * 0.50:.2f}")
                else:
                    QMessageBox.about(self, "Aviso", "Livro devolvido com sucesso!")
                self.tela_pricipal.tabela_emprestimos.removeRow(linha)
        else:
            QMessageBox.about(self, "Erro", "Livro não encontrado!")

    def enviar_login(self):
        email = self.tela_login.caixa_email.text()
        senha = self.tela_login.caixa_senha.text()
        if email and senha:
            client_socket.send(f"2,{email},{senha}".encode())
            resposta = client_socket.recv(1024).decode().split(',')
            if resposta[0] == "2":
                if resposta[1] == "1":
                    self.QtStack.setCurrentIndex(2)
                else:
                    self.atualizar_emprestimos()
                    self.QtStack.setCurrentIndex(1)
            else:
                QMessageBox.about(self, "Erro", "Email ou senha incorretos!")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos!")

    def botao_sair(self):
        client_socket.send("0".encode())
        self.tela_pricipal.limpar(self.tela_pricipal.tabela_emprestimos)
        self.tela_pricipal.limpar(self.tela_pricipal.tabela_livros)
        self.tela_pricipal.caixa_buscar.clear()
        self.tela_pricipal.caixa_devolver.clear()
        self.QtStack.setCurrentIndex(0)

    def botao_fechar(self):
        client_socket.send("-1".encode())
        client_socket.close()
        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())