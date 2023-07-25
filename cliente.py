import typing   #biblioteca usada para fornecer suporte a anotações de tipo ou seja, permite definir e trabalhar com diferentes tipos de argumentos nos metodos
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
import random
import os
from hashlib import md5

from pessoa import Pessoa
from usuario import Usuario
from autor import Autor
from biblioteca import Biblioteca
from livro import Livro
from exemplar import Exemplar
from emprestimo import Emprestimo
from devolucao import Devolucao



from tela_biblioteca import Tela_Biblioteca
from tela_biblioteca_usuario import Tela_Biblioteca_Usuario
from tela_login import Tela_Login
from tela_cadastro import Tela_Cadastro
from tela_buscar_cadastro import Tela_Buscar_Cadastro
from tela_autor import Tela_Autor
from tela_buscar_autor import Tela_Buscar_Autor
from tela_livro import Tela_Livro
from tela_buscar_livro import Tela_Buscar_Livro
from tela_exemplar import Tela_Exemplar
from tela_buscar_exemplar import Tela_Buscar_Exemplar
from tela_emprestimo import Tela_Emprestimo
from tela_buscar_emprestimo import Tela_Buscar_Emprestimo
from tela_devolucao import Tela_Devolucao
from tela_buscar_devolucao import Tela_Buscar_Devolucao

import mysql.connector 
 
import socket
ip = host = socket.gethostbyname(socket.gethostname())
port = 8080
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(addr)
except:
    print("\nNao foi possivel se conectar ao servidor!\n")
    exit()

class Ui_Main(QtWidgets.QWidget):
    """
    Classe que apresenta todas as telas necessárias para a aplicação do prototipo do sistema

    ...

    Attributes
    ----------
    stack : objeto
        utilizado para representar uma lista como pilhas. A mesma representa uma pilha de metodos do prototipo do sistema.
    
    tela_login : class
        tela de login
    tela_cadastro : class
        tela de cadastro
    buscar_cadastro : class
        tela buscar cadastro 
    tela_biblioteca : class
        tela principal da biblioteca para administrador(es) do sistema
    tela_biblioteca_usuario : class
        tela principal da biblioteca para usuarios do sistema
    tela_autor : class
        tela de cadastro de autor para administrador do sistema
    tela_buscar_autor : class
        tela buscar autor
    tela_livro : class
        tela de cadastro de livro para administrador do sistema
    tela_buscar_livro : class
        tela buscar livro
    tela_exemplar : class
        tela de cadastro de exemplar de livro para administrador do sistema
    tela_buscar_exemplar : class
        tela buscar exemplar
    tela_emprestimo : class
        tela de emprestimo de exemplar de livro
    tela_buscar_emprestimo : class
        tela buscar emprestimo
    tela_devolucao : class
        tela de devolucoes de exemplar de livro
    tela_buscar_devolucao : class
        tela buscar devolucao
    
    
    """
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack0 = QtWidgets.QMainWindow()  #login
        self.stack1 = QtWidgets.QMainWindow()  #cadastro
        self.stack2 = QtWidgets.QMainWindow()  #buscar cadastro
        self.stack3 = QtWidgets.QMainWindow()  #biblioteca admin
        self.stack4 = QtWidgets.QMainWindow()  #biblioteca usuario
        self.stack5 = QtWidgets.QMainWindow()  #cadastrar autor
        self.stack6 = QtWidgets.QMainWindow()  #buscar autor
        self.stack7 = QtWidgets.QMainWindow()  #livro
        self.stack8 = QtWidgets.QMainWindow()  #buscar livro
        self.stack9 = QtWidgets.QMainWindow()  #cadastrar exemplar
        self.stack10 = QtWidgets.QMainWindow() #buscar exemplar
        self.stack11 = QtWidgets.QMainWindow() #cadastrar emprestimo
        self.stack12 = QtWidgets.QMainWindow() #buscar emprestimo
        self.stack13 = QtWidgets.QMainWindow() #cadastrar devolucao
        self.stack14 = QtWidgets.QMainWindow() #buscar devolucao

        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack0)
        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)
        self.tela_buscar_cadastro = Tela_Buscar_Cadastro()
        self.tela_buscar_cadastro.setupUi(self.stack2)
        self.tela_biblioteca = Tela_Biblioteca()
        self.tela_biblioteca.setupUi(self.stack3)
        self.tela_biblioteca_usuario = Tela_Biblioteca_Usuario()
        self.tela_biblioteca_usuario.setupUi(self.stack4)
        self.tela_autor = Tela_Autor()
        self.tela_autor.setupUi(self.stack5)
        self.tela_buscar_autor = Tela_Buscar_Autor()
        self.tela_buscar_autor.setupUi(self.stack6)
        self.tela_livro = Tela_Livro()
        self.tela_livro.setupUi(self.stack7)
        self.tela_buscar_livro = Tela_Buscar_Livro()
        self.tela_buscar_livro.setupUi(self.stack8)
        self.tela_exemplar = Tela_Exemplar()
        self.tela_exemplar.setupUi(self.stack9)
        self.tela_buscar_exemplar = Tela_Buscar_Exemplar()
        self.tela_buscar_exemplar.setupUi(self.stack10)
        self.tela_emprestimo = Tela_Emprestimo()
        self.tela_emprestimo.setupUi(self.stack11)
        self.tela_buscar_emprestimo = Tela_Buscar_Emprestimo()
        self.tela_buscar_emprestimo.setupUi(self.stack12)
        self.tela_devolucao = Tela_Devolucao()
        self.tela_devolucao.setupUi(self.stack13)
        self.tela_buscar_devolucao = Tela_Buscar_Devolucao()
        self.tela_buscar_devolucao.setupUi(self.stack14)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)
        self.QtStack.addWidget(self.stack12)
        self.QtStack.addWidget(self.stack13)
        self.QtStack.addWidget(self.stack14)

    

class Main(QMainWindow, Ui_Main):
    """
    classe principal que executa todos os metodos e acoes das telas e seus respectivos botoes, a nivel de comunicacao com cliente.


    Attributes
    ----------
    
    
    
    Methods
    -------
    init():
        recebe os objetos de conexao das telas com seus respectivos botoes
    abrirTelaLogin():
        abre a tela de login
    botao_Login():
        realiza login para ter acesso as funcionalidades do sistema
    abrirTelaCadastro():
        abre a tela de login
    botao_Cadastrar_Usuario():
        realiza cadastro de um usuario, caso o mesmo nao possua
    botao_Voltar_Cadastro():
        volta da tela de cadastro para a de login
    abrirTelaBibliotecaUsuario():
        abre a tela principal da biblioteca
    abrirTelaBuscarCadastro():
        abre a tela de buscar cadastro
    botao_Buscar_Usuario():
        faz a busca de usuario do sistema pelo seu codigo de cadastro
    botao_Voltar_Buscar_usuario():
        volta da tela buscar usuario para a tela principal
    abrirTelaAutor():
        abre a tela de cadastro de autor para adminitrador do sistema
    botao_Cadastrar_Autor():
        realiza o cadastro de um autor
    botao_Voltar_Autor():
        volta da tela ator para a tela principal
    abrirTelaBuscarAutor:
        abre a tela buscar autor
    botao_Buscar_Autor:
        realiza a busca de um autor pelo seu nome
    botao_Voltar_Buscar_Autor:
        volta da tela buscar autor para a tela principal
    abrirTelaLivro():
    botao_Cadastrar_Livro():
        realiza o cadastro de livro
    botao_Voltar_Livro():
        volta da tela livro para a tela principal
    abrirTelaBuscarLivro():
        abre a tela buscar livro
    botao_Buscar_Livro():
        realiza a busca de um livro pelo seu codigo
    botao_Voltar_Buscar_Livro():
        volta da tela buscar livro para a tela principal
    abrirTelaExemplar():
        abre a tela de cadastro de um exemplar
    botao_Cadastrar_Exemplar():
        realiza o cadastro de um exemplar de livro
    botao_Voltar_Exemplar():
        volta da tela exemplar para a tela principal
    botao_Voltar_Biblioteca():
        volta da tela principal para a tela de login
    abrirTelaBuscarExemplar():
        abre a tela buscar exemplar
    botao_Buscar_Exemplar():
        realiza a busca de um exemplar pelo seu codigo
    botao_Voltar_Buscar_Exemplar():
        volta da tela buscar exemplar para a tela principal
    abrirTelaEmprestimo():
        abre a tela de emprestimo
    botao_Realizar_Emprestimo:
        realiza emprestimo de exemplar de livro
    botao_Voltar_Emprestimo:
        volta da tela de emprestimo para a tela principal
    abrirTelaBuscarEmprestimo:
        abre a tela buscar emprestiimo
    botao_Buscar_Emprestimo
        realiza a busca de emprestimo de exemplar de livro pelo codigo do exemplar
    botao_Voltar_Buscar_Emprestimo:
        volta da tela buscar emprestimo para a tela principal
    abrirTelaDevolucao:
        abre a tela de devolucao de exemplar
    botao_Devolver:
        realiza a devolucao de um exemplar de livro
    botao_Voltar_Devolucao:
        volta da tela de devolucao para a tela principal
    abrirTelaBuscarDevolucao:
        abre a tela buscar devolucao
    botao_Buscar_Devolucao:
        realiza a busca de devolucoes de exemplares de livro pelo codigo do exemplar e data da devolucao
    botao_Voltar_Buscar_Devolucao:
        volta da tela buscar devolucao para a tela principal
    botao_Voltar_Biblioteca_Usuario:
        volta da tela principal de biblioteca para a tela de login
    botao_sair_login:
        botao para sair do sistema.

    """
    def __init__(self, parent = None):
        #self.usuario = None
        verificarLogin = list()
        super(Main, self).__init__(parent)
        self.setupUi(self)

        # conexao de multitelas a partir da tela biblioteca criada 

        self.bib = Biblioteca()
        #tela de login e cadastro para todos os usuarios
        
        self.tela_login.botao_login.clicked.connect(self.botao_Login)
        self.tela_login.botao_cadastro_login.clicked.connect(self.abrirTelaCadastro)
        self.tela_login.botao_sair_login.clicked.connect(self.abrirTelaBiblioteca)

        self.tela_cadastro.botao_cadastrar_usuario.clicked.connect(self.abrirTelaCadastro)
        self.tela_cadastro.botao_cadastrar_usuario.clicked.connect(self.botao_Cadastrar_Usuario)
        self.tela_cadastro.botao_voltar_cadastro.clicked.connect(self.botao_Voltar_Cadastro)

        '''telas de cadastros para administrador'''
        #cadastrar autor
        self.tela_biblioteca.botao_cadastrar_autor_biblioteca.clicked.connect(self.abrirTelaAutor)
        self.tela_autor.botao_cadastrar_autor.clicked.connect(self.botao_Cadastrar_Autor)
        self.tela_autor.botao_voltar_autor.clicked.connect(self.botao_Voltar_Autor)
        #cadastrar livro
        self.tela_biblioteca.botao_cadastrar_livro_biblioteca.clicked.connect(self.abrirTelaLivro)
        self.tela_livro.botao_cadastrar_livro.clicked.connect(self.botao_Cadastrar_Livro)
        self.tela_livro.botao_voltar_livro.clicked.connect(self.botao_Voltar_Livro)
        #cadastrar exemplar
        self.tela_biblioteca.botao_cadastrar_exemplar_biblioteca.clicked.connect(self.abrirTelaExemplar)
        self.tela_exemplar.botao_cadastrar_exemplar.clicked.connect(self.botao_Cadastrar_Exemplar)
        self.tela_exemplar.botao_voltar_exemplar.clicked.connect(self.botao_Voltar_Exemplar)

        self.tela_biblioteca.botao_voltar_biblioteca_admin.clicked.connect(self.botao_Voltar_Biblioteca)


        '''telas de busca, emprestimo e devolucao para usuarios'''
        #buscar usuario pelo codigo do usuario
        self.tela_biblioteca_usuario.botao_buscar_cadastro_biblioteca_usuario.clicked.connect(self.abrirTelaBuscarCadastro)
        self.tela_buscar_cadastro.botao_buscar_usuario.clicked.connect(self.botao_Buscar_Usuario)
        self.tela_buscar_cadastro.boto_voltar_buscar.clicked.connect(self.botao_Voltar_Buscar_usuario)
        #buscar autor por nome
        self.tela_biblioteca_usuario.botao_buscar_autor_biblioteca_usuario.clicked.connect(self.abrirTelaBuscarAutor)
        self.tela_buscar_autor.botao_buscar_autor.clicked.connect(self.botao_Buscar_Autor)
        self.tela_buscar_autor.botao_voltar_buscar_autor.clicked.connect(self.botao_Voltar_Buscar_Autor)
        #buscar livro por codigo do livro
        self.tela_biblioteca_usuario.botao_buscar_livro_biblioteca_usuario.clicked.connect(self.abrirTelaBuscarLivro)
        self.tela_buscar_livro.botao_buscar_livro.clicked.connect(self.botao_Buscar_Livro)
        self.tela_buscar_livro.botao_voltar_buscar_livro.clicked.connect(self.botao_Voltar_Buscar_Livro)
        #buscar exemplar por codigo do exemplar
        self.tela_biblioteca_usuario.botao_buscar_exemplar_biblioteca_usuario.clicked.connect(self.abrirTelaBuscarExemplar)
        self.tela_buscar_exemplar.botao_buscar_exemplar.clicked.connect(self.botao_Buscar_Exemplar)
        self.tela_buscar_exemplar.botao_voltar_busca_exemplar.clicked.connect(self.botao_Voltar_Buscar_Exemplar)
        #realizar emprestimo
        self.tela_biblioteca_usuario.botao_emprestimo_biblioteca_usuario.clicked.connect(self.abrirTelaEmprestimo)
        self.tela_emprestimo.botao_realizar_emprestimo.clicked.connect(self.botao_Realizar_Emprestimo)
        self.tela_emprestimo.botao_voltar_realizar_emprestimo.clicked.connect(self.botao_Voltar_Emprestimo)
        #buscar emprestimo por codigo do exemplar
        self.tela_biblioteca_usuario.botao_buscar_emprestimo_biblioteca_usuario.clicked.connect(self.abrirTelaBuscarEmprestimo)
        self.tela_buscar_emprestimo.botao_buscar_emprestimo.clicked.connect(self.botao_Buscar_Emprestimo)
        self.tela_buscar_emprestimo.botao_devolver.clicked.connect(self.abrirTelaDevolucao)
        self.tela_buscar_emprestimo.botao_voltar_buscar_emprestimo.clicked.connect(self.botao_Voltar_Buscar_Emprestimo)
        #realizar devolucao
        self.tela_biblioteca_usuario.botao_devolucao_biblioteca_usuario.clicked.connect(self.abrirTelaDevolucao)
        self.tela_devolucao.botao_devolver.clicked.connect(self.botao_Devolver)
        self.tela_devolucao.botao_voltar_devolucao.clicked.connect(self.botao_Voltar_Devolucao)
        #buscar devolucao
        self.tela_biblioteca_usuario.botao_buscar_devolucao_biblioteca_usuario.clicked.connect(self.abrirTelaBuscarDevolucao)
        self.tela_buscar_devolucao.botao_buscar_devolucao.clicked.connect(self.botao_Buscar_Devolucao)
        self.tela_buscar_devolucao.botao_voltar_buscar_devolucao.clicked.connect(self.botao_Voltar_Buscar_Devolucao)

        self.tela_biblioteca_usuario.botao_voltar_biblioteca_usuario.clicked.connect(self.botao_Voltar_Biblioteca_Usuario)

        self.tela_login.botao_sair_login.clicked.connect(self.botao_sair_login) #botao para sair do sistema bibliotecario

    def abrirTelaLogin(self):  # Método para abrir a tela de cadastro
        self.QtStack.setCurrentIndex(0)

    def botao_Login(self):  # Método para ativar as funcionalidades do botao login
        
        codigo_usuario = self.tela_login.input_usuario.text()
        senha = self.tela_login.input_senha.text()

        if not (codigo_usuario == "" or senha == ""):   # verifica se todos os campos foram preenchidos
            client_socket.send('2'.encode())

            lista_de_login = []
            lista_de_login.append(codigo_usuario)
            lista_de_login.append(senha)
            dados = ",".join(lista_de_login)
            client_socket.send(dados.encode())
            confirmacao = client_socket.recv(4096).decode().split(',')
            if confirmacao[0] == '0':
                QMessageBox.information(None, 'Atenção!', 'código de usuário não cadastrado!')
                self.tela_login.input_usuario.setText("")  # limpar campo de input
            elif confirmacao[0] == '1':
                QMessageBox.information(None, 'Atenção!', 'Senha incorreta!')
                self.tela_login.input_senha.setText("")
            elif confirmacao[0] == '2':
                QMessageBox.information(None, "POO2", "Usuário logado no sistema!")
                self.usuario = Usuario(*confirmacao[1:])
                if self.usuario.tipo == 'admin':
                    self.tela_login.input_usuario.setText("")  # limpar campo de input
                    self.tela_login.input_senha.setText("")
                    self.abrirTelaBiblioteca()  # Método para abrir a tela de login
                elif self.usuario.tipo =='usuario':
                    self.tela_login.input_usuario.setText("")  # limpar campo de input
                    self.tela_login.input_senha.setText("")
                    self.abrirTelaBibliotecaUsuario()
            else:
                QMessageBox.information(None,"Atenção!"," Usuário não cadastrado!")  # mensagem de erro
                self.tela_login.input_usuario.setText("")
                self.tela_login.input_senha.setText("")
                self.abrirTelaCadastro()
        else:
            QMessageBox.information(None, "Atenção!", "Todos os campos devem ser preenchidos!")
        
            

    def abrirTelaCadastro(self):  # Método para abrir a tela de cadastro
        self.QtStack.setCurrentIndex(1)

    # Método para ativar o botão cadastrar
    def botao_Cadastrar_Usuario(self):
        nome = self.tela_cadastro.input_nome.text()
        codigo_usuario = self.tela_cadastro.input_codigo.text()
        cpf = self.tela_cadastro.input_cpf.text()
        telefone = self.tela_cadastro.input_fone.text()
        endereco = self.tela_cadastro.input_endereco.text()
        bairro = self.tela_cadastro.input_bairro.text()
        cidade = self.tela_cadastro.input_cidade.text()
        cep = self.tela_cadastro.input_cep.text()
        email = self.tela_cadastro.input_email.text()
        senha = self.tela_cadastro.input_senha.text()
        # verifica se todos os campos foram preenchidos
        tipo = 'usuario'
        if not (nome == "" or codigo_usuario == ""or cpf == ""or telefone == ""or endereco == ""or bairro == ""or cidade == ""or cep == ""or email == ""or senha == ""):
            client_socket.send('1'.encode())
            self.tela_cadastro.input_nome.setText("")
            self.tela_cadastro.input_codigo.setText("")
            self.tela_cadastro.input_cpf.setText("")
            self.tela_cadastro.input_fone.setText("")
            self.tela_cadastro.input_endereco.setText("")
            self.tela_cadastro.input_bairro.setText("")
            self.tela_cadastro.input_cidade.setText("")
            self.tela_cadastro.input_cep.setText("")
            self.tela_cadastro.input_email.setText("")
            self.tela_cadastro.input_senha.setText("")

            lista_de_dados = []
            lista_de_dados.append(codigo_usuario)
            lista_de_dados.append(nome)
            lista_de_dados.append(cpf)
            lista_de_dados.append(telefone)
            lista_de_dados.append(endereco)
            lista_de_dados.append(bairro)
            lista_de_dados.append(cidade)
            lista_de_dados.append(cep)
            lista_de_dados.append(email)
            lista_de_dados.append(senha)
            lista_de_dados.append(tipo)
            dados = ",".join(lista_de_dados)
            client_socket.send(dados.encode())

            try:
                retorno = client_socket.recv(4096).decode()
            except:
                print("\nNao foi possivel permanecer conectado!\n")
                print("\nnPressione <Enter> para continuar...")
                client_socket.close()
            if(retorno == '1'):
                QMessageBox.information(None, "Olá!", "Usuario Cadastrado com Sucesso!")
                self.botao_Voltar_Cadastro()

            elif(retorno == '0'):
                QMessageBox.information(None,"Atenção!","O CPF informado já está cadastrado na base de dados!")   
        
        else:
            QMessageBox.information(None, "Atenção!", "Todos os valores devem ser preenchidos!")

    def botao_Voltar_Cadastro(self):  # Método para ativar o botão voltar
        self.usuario = None
        self.QtStack.setCurrentIndex(0)

    def abrirTelaBibliotecaUsuario(self):  # Método para abrir a tela de login
        self.QtStack.setCurrentIndex(4)

    
    def abrirTelaBuscarCadastro(self):  # Método para abrir a tela de cadastro
        self.QtStack.setCurrentIndex(2)

    def botao_Buscar_Usuario(self):  # Método para ativar as funcionalidades de busca no botão buscar
        codigo_usuario = self.tela_buscar_cadastro.input_codigo_usuario2.text()
        usuario = self.bib.buscarUsuario(codigo_usuario)
        if (usuario != None):
            client_socket.send('3'.encode())
        
            self.tela_buscar_cadastro.input_nome2.setText(usuario.nome)
            self.tela_buscar_cadastro.input_cpf2.setText(usuario.cpf)
            self.tela_buscar_cadastro.input_fone2.setText(usuario.telefone)
            self.tela_buscar_cadastro.input_endeco2.setText(usuario.endereco)
            self.tela_buscar_cadastro.input_bairro2.setText(usuario.bairro)
            self.tela_buscar_cadastro.input_cidade2.setText(usuario.cidade)
            self.tela_buscar_cadastro.input_cep2.setText(usuario.cep)
            self.tela_buscar_cadastro.input_email2.setText(usuario.email)
            self.tela_buscar_cadastro.input_senha2.setText(usuario.senha)

            lista_usuarios = []
            lista_usuarios.append(usuario.nome)
            lista_usuarios.append(usuario.cpf)
            lista_usuarios.append(usuario.telefone)
            lista_usuarios.append(usuario.endereco)
            lista_usuarios.append(usuario.bairro)
            lista_usuarios.append(usuario.cidade)
            lista_usuarios.append(usuario.cep)
            lista_usuarios.append(usuario.email)
            lista_usuarios.append(usuario.senha)
            lista_usuarios.append(Main.login[1])
            dados_usuarios = ",".join(lista_usuarios)
            client_socket.send(dados_usuarios.encode())
            retorno = client_socket.recv(4096).decode()

            
        else:
            QMessageBox.information(None, "POO2", "Usuario não encontrado!")
    
    def botao_Voltar_Buscar_usuario(self):  # Método para ativar o botão voltar
        self.QtStack.setCurrentIndex(4)

    
    def abrirTelaBiblioteca(self):  # Método para abrir a tela de login
        self.QtStack.setCurrentIndex(3)

    def abrirTelaAutor(self):  # Método para abrir a tela autor
        self.QtStack.setCurrentIndex(5)

    def botao_Cadastrar_Autor(self):  # Método para ativar o botão cadastrar autor
        nome_autor = self.tela_autor.input_nome_autor.text()
        codigo_autor = self.tela_autor.input_codigo_autor.text()
        if not (nome_autor == "" or codigo_autor == ""):
            client_socket.send('4'.encode())
            
            #autor = Autor(codigo_autor, nome_autor)
            #if (self.bib.cadastrarAutor(autor)) == True:
                
            self.tela_autor.input_nome_autor.setText("")
            self.tela_autor.input_codigo_autor.setText("")
            lista_autor=[]
            lista_autor.append(nome_autor)
            lista_autor.append(codigo_autor)
            dados_autor = ",".join(lista_autor)
            client_socket.send(dados_autor.encode())
            
            retorno = client_socket.recv(4096).decode()
            
            if(retorno == '1'):
                QMessageBox.information(None, "Olá", "Autor cadastrado com sucesso!")
                self.abrirTelaLivro()
            elif(retorno == '0'):
                QMessageBox.information(None,"Atenção!","Este autor já está cadastrado na base de dados!")   
        
        else:
            QMessageBox.information(None, "Atenção!", "Todos os campos devem ser preenchidos!")


    def botao_Voltar_Autor(self):  # Método para ativar o botão voltar da tela autor
        self.QtStack.setCurrentIndex(3)


    def abrirTelaBuscarAutor(self):  # Método para abrir a tela autor
        self.QtStack.setCurrentIndex(6)

    def botao_Buscar_Autor(self):  # Método para ativar as funcionalidades de busca no botão buscar autor
        nome_autor = self.tela_buscar_autor.input_nome_autor_2.text()
        autor = self.bib.buscarAutores(nome_autor)
        if (autor != None):
            self.tela_buscar_autor.input_codigo_autor_2.setText(autor.codigo_autor)
        
        else:
            QMessageBox.information(None, "POO2", "Autor não cadastrado!")

    def botao_Voltar_Buscar_Autor(self):  # Método para ativar o botão voltar da tela autor
        self.QtStack.setCurrentIndex(4)


    def abrirTelaLivro(self):  # Método para abrir a tela de livro
        self.QtStack.setCurrentIndex(7)

    def botao_Cadastrar_Livro(self):  # Método para ativar o botão cadastrar
        nome_autor = self.tela_livro.input_nome_autor.text()
        codigo_autor = self.tela_livro.input_codigo_autor.text()
        titulo = self.tela_livro.input_titulo_livro.text()
        codigo_livro = self.tela_livro.input_codigo_livro.text()
        assunto = self.tela_livro.input_assunto.text()
        isbn = self.tela_livro.input_isbn.text()
        editora = self.tela_livro.input_editora.text()
        edicao = self.tela_livro.input_edicao.text()
        volume = self.tela_livro.input_volume.text()
        Numero_pag = self.tela_livro.input_num_paginas.text()
        anoPublicacao = self.tela_livro.input_ano_publicacao.text()
        
        if not (nome_autor == "" or codigo_autor == "" or titulo == "" or codigo_livro == "" or assunto == "" or isbn == "" or editora == "" or edicao == "" or volume == "" or Numero_pag == "" or anoPublicacao == ""):
            #livro = Livro(codigo_livro, nome_autor, codigo_autor, titulo, editora, isbn, assunto, edicao, volume, Numero_pag, anoPublicacao)
            #if (self.bib.cadastrarLivros(livro)) == True:
            client_socket.send('6'.encode())
                
            self.tela_livro.input_nome_autor.setText("")
            self.tela_livro.input_codigo_autor.setText("")
            self.tela_livro.input_titulo_livro.setText("")
            self.tela_livro.input_codigo_livro.setText("")
            self.tela_livro.input_assunto.setText("")
            self.tela_livro.input_isbn.setText("")
            self.tela_livro.input_editora.setText("")
            self.tela_livro.input_edicao.setText("")
            self.tela_livro.input_volume.setText("")
            self.tela_livro.input_num_paginas.setText("")
            self.tela_livro.input_ano_publicacao.setText("")
                
            lista_livro=[]
            lista_livro.append(nome_autor)
            lista_livro.append(codigo_autor)
            lista_livro.append(titulo)
            lista_livro.append(codigo_livro)
            lista_livro.append(assunto)
            lista_livro.append(isbn)
            lista_livro.append(editora)
            lista_livro.append(edicao)
            lista_livro.append(volume)
            lista_livro.append(Numero_pag)
            lista_livro.append(anoPublicacao)
            dados_livro = ",".join(lista_livro)
            client_socket.send(dados_livro.encode())

            retorno = client_socket.recv(4096).decode() 
            if(retorno == '1'):
                QMessageBox.information(None, "Olá", "Livro cadastrado com sucesso!")
                self.abrirTelaExemplar()
            elif(retorno == '0'):
                QMessageBox.information(None,"Atenção!","Este livro já está cadastrado na base de dados!")   
        else:
            QMessageBox.information(None, "Atenção!", "Todos os campos devem ser preenchidos!")


    def botao_Voltar_Livro(self):  # Método para ativar o botão voltar da tela livro
        self.QtStack.setCurrentIndex(3)
    

    def abrirTelaBuscarLivro(self):  # Método para abrir a tela buscar livro
        self.QtStack.setCurrentIndex(8)

    def botao_Buscar_Livro(self):  # Método para ativar o botão buscar livro
        codigo_livro = self.tela_buscar_livro.input_cod_livro2.text()
        livro = self.bib.buscarLivros(codigo_livro)
        if (livro != None):
            self.tela_buscar_livro.input_nome_autor2.setText(livro.nome_autor)
            self.tela_buscar_livro.input_cod_autor2.setText(livro.codigo_autor)
            self.tela_buscar_livro.input_titulo_livro2.setText(livro.titulo)
            self.tela_buscar_livro.input_editora2.setText(livro.editora)
            self.tela_buscar_livro.input_ano_publicacao2.setText(livro.anoPublicacao)
            self.tela_buscar_livro.input_isbn2.setText(livro.isbn)
            self.tela_buscar_livro.input_assunto2.setText(livro.assunto)
            self.tela_buscar_livro.input_edicao2.setText(livro.edicao)
            self.tela_buscar_livro.input_num_paginas2.setText(livro.Numero_pag)
            self.tela_buscar_livro.input_volume2.setText(livro.volume)
        else:
            QMessageBox.information(None, "POO2", "Livro não cadastrado no sistema!")

    def botao_Voltar_Buscar_Livro(self):  # Método para ativar o botão voltar da tela autor
        self.QtStack.setCurrentIndex(4)


    def abrirTelaExemplar(self):  # Método para abrir a tela de exemplar
        self.QtStack.setCurrentIndex(9)

    def botao_Cadastrar_Exemplar(self):  # Método para ativar o botão cadastrar exemplar
        codigo_livro = self.tela_exemplar.input_codigo_livro.text()
        codigo_exemplar = self.tela_exemplar.input_codigo_exemplar.text()
        dias_emprestimo = self.tela_exemplar.input_qtd_dias.text()
        if not (codigo_livro == "" or codigo_exemplar == "" or dias_emprestimo == ""):
            client_socket.send('8'.encode())
            #exemplar = Exemplar(codigo_exemplar,codigo_livro,dias_emprestimo)
            #if (self.bib.cadastrarExemplares(exemplar)) == True:
                
            self.tela_exemplar.input_codigo_livro.setText("")
            self.tela_exemplar.input_codigo_exemplar.setText("")
            self.tela_exemplar.input_qtd_dias.setText("")
            lista_exemplar = []
            lista_exemplar.append(codigo_exemplar)
            lista_exemplar.append(codigo_livro)
            lista_exemplar.append(dias_emprestimo)
            dados_exemplar = ",".join(lista_exemplar)
            client_socket.send(dados_exemplar.encode())
            retorno = client_socket.recv(4096).decode() 
            if(retorno == '1'):
                QMessageBox.information(None, "Olá", "Exemplar cadastrado com sucesso!")
                self.abrirTelaBiblioteca()
            elif(retorno == '0'):
                QMessageBox.information(None,"Atenção!","Este exemplar já está cadastrado na base de dados!")   
        else:
            QMessageBox.information(None, "Atenção!", "Todos os campos devem ser preenchidos!")

    def botao_Voltar_Exemplar(self):  # Método para ativar o botão voltar da tela exemplar
        self.QtStack.setCurrentIndex(3)
    

    def botao_Voltar_Biblioteca(self):  # Método para ativar o botão voltar da tela autor
        self.QtStack.setCurrentIndex(0)
    

    def abrirTelaBuscarExemplar(self):  # Método para abrir a tela de exemplar
        self.QtStack.setCurrentIndex(10)

    def botao_Buscar_Exemplar(self):  # Método para ativar o botão buscar exemplar
        codigo_exemplar = self.tela_buscar_exemplar.input_codigo_exemplar2.text()
        exemplar = self.bib.buscarExemplares(codigo_exemplar)
        if (exemplar != None):
            self.tela_buscar_exemplar.input_codigo_livro2.setText(exemplar.codigo_livro)
            self.tela_buscar_exemplar.input_qtd_dias2.setText(exemplar.dias_emprestimo)
        else:
            QMessageBox.information(None, "POO2", "O exemplar não esta cadastrado na base de dados do sistema!")

    def botao_Voltar_Buscar_Exemplar(self):  # Método para ativar o botão voltar da tela exemplar
        self.QtStack.setCurrentIndex(4)


    def abrirTelaEmprestimo(self):  # Método para abrir a tela de emprestimo
        self.QtStack.setCurrentIndex(11)

    def botao_Realizar_Emprestimo(self):  # Método para ativar o botão cadastrar emprestimos
        codigo_usuario = self.tela_emprestimo.input_codigo_usuario.text()
        codigo_exemplar = self.tela_emprestimo.input_codigo_exemplar.text()
        codigo_livro = self.tela_emprestimo.input_codigo_livro.text()
        data_emprestimo = self.tela_emprestimo.input_data_emprestimo.text()
        data_para_devolver = self.tela_emprestimo.input_data_devolucao.text()
        if not (codigo_usuario == "" or codigo_exemplar == "" or codigo_livro == "" or data_emprestimo == "" or data_para_devolver == ""):
            #emprestimo = Emprestimo(codigo_usuario,codigo_livro,codigo_exemplar,data_emprestimo,data_para_devolver)
            #if (self.bib.realizarEmprestimo(emprestimo)) == True:
            client_socket.send('10'.encode())    
            
            self.tela_emprestimo.input_codigo_usuario.setText("")
            self.tela_emprestimo.input_codigo_exemplar.setText("")
            self.tela_emprestimo.input_codigo_livro.setText("")
            self.tela_emprestimo.input_data_emprestimo.setText("")
            self.tela_emprestimo.input_data_devolucao.setText("")
            lista_emprestimo = []
            lista_emprestimo.append(codigo_usuario)
            lista_emprestimo.append(codigo_exemplar)
            lista_emprestimo.append(codigo_livro)
            lista_emprestimo.append(data_emprestimo)
            lista_emprestimo.append(data_para_devolver)
            dados_emprestimo = ",".join(lista_emprestimo)
            client_socket.send(dados_emprestimo.encode())
            retorno = client_socket.recv(4096).decode() 
            if(retorno == '1'):
                QMessageBox.information(None, "Olá", "Emprestimo realizado com sucesso!")
                self.abrirTelaBibliotecaUsuario()
            elif(retorno == '0'):
                QMessageBox.information(None,"Atenção!","Este exemplar já possui registro de emprestimo na base de dados do sistema!")   
        else:
            QMessageBox.information(None, "Atenção!", "Todos os campos devem ser preenchidos!")

    def botao_Voltar_Emprestimo(self):  # Método para ativar o botão voltar da tela emprestimo
        self.QtStack.setCurrentIndex(4)
    

    def abrirTelaBuscarEmprestimo(self):  # Método para abrir a tela de emprestimo
        self.QtStack.setCurrentIndex(12)
    
    def botao_Buscar_Emprestimo(self):  # Método para ativar o botão buscar emprestimo
        codigo_exemplar = self.tela_buscar_emprestimo.input_codigo_exemplar2.text()
        emprestimo = self.bib.buscarEmprestimo(codigo_exemplar)
        if (emprestimo != None):
            self.tela_buscar_emprestimo.input_codigo_livro2.setText(emprestimo.codigo_livro)
            self.tela_buscar_emprestimo.input_data_emprestimo2.setText(emprestimo.data_emprestimo)
            self.tela_buscar_emprestimo.input_data_devolucao2.setText(emprestimo.data_para_devolver)
        else:
            QMessageBox.information(None, "POO2", "O exemplar não possui registro de emprestimo!")

    def botao_Voltar_Buscar_Emprestimo(self):  # Método para ativar o botão voltar da tela emprestimo
        self.QtStack.setCurrentIndex(4)
    

    def abrirTelaDevolucao(self):  # Método para abrir a tela de emprestimo
        self.QtStack.setCurrentIndex(13)
        
    def botao_Devolver(self):
        codigo_usuario = self.tela_devolucao.input_codigo_usuario.text()
        codigo_exemplar = self.tela_devolucao.input_codigo_exemplar.text()
        codigo_livro = self.tela_devolucao.input_codigo_livro.text()
        data_emprestimo = self.tela_devolucao.input_data_emprestimo.text()
        data_devolucao = self.tela_devolucao.input_data_devolucao.text()
        if not (codigo_usuario == "" or codigo_exemplar == "" or codigo_livro == "" or data_emprestimo == "" or data_devolucao == ""):
            #devolucao = Devolucao(codigo_usuario, codigo_livro, codigo_exemplar, data_emprestimo, data_devolucao)
            #if (self.bib.realizarDevolucao(devolucao)) == True:
            client_socket.send('12'.encode())    
            self.tela_devolucao.input_codigo_usuario.setText("")
            self.tela_devolucao.input_codigo_exemplar.setText("")
            self.tela_devolucao.input_codigo_livro.setText("")
            self.tela_devolucao.input_data_emprestimo.setText("")
            self.tela_devolucao.input_data_devolucao.setText("")
            lista_devolucao = []
            lista_devolucao.append(codigo_usuario)
            lista_devolucao.append(codigo_exemplar)
            lista_devolucao.append(codigo_livro)
            lista_devolucao.append(data_emprestimo)
            lista_devolucao.append(data_devolucao)
            dados_devolucao = ",".join(lista_devolucao)
            client_socket.send(dados_devolucao.encode())
            retorno = client_socket.recv(4096).decode() 
            if(retorno == '1'):
                QMessageBox.information(None, "Olá", "Devolução realizada com sucesso!")
                self.abrirTelaBibliotecaUsuario()
            elif(retorno == '0'):
                QMessageBox.information(None,"Atenção!","Este exemplar já possui registro de devolucao na base de dados do sistema!")   
        else:
            QMessageBox.information(None, "Atenção!", "Todos os campos devem ser preenchidos!")

    def botao_Voltar_Devolucao(self):  # Método para ativar o botão voltar da tela emprestimo
        self.QtStack.setCurrentIndex(4)
    
    
    def abrirTelaBuscarDevolucao(self):  # Método para abrir a tela de emprestimo
        self.QtStack.setCurrentIndex(14)
    
    def botao_Buscar_Devolucao(self):
        codigo_exemplar = self.tela_buscar_devolucao.input_codigo_exemplar_2.text()
        data_devolucao = self.tela_buscar_devolucao.input_data_devolucao_2.text()
        devolucao = self.bib.buscarDevolucoes(codigo_exemplar, data_devolucao)
        if (devolucao != None):
            self.tela_buscar_devolucao.input_codigo_livro_2.setText(devolucao.codigo_livro)
            self.tela_buscar_devolucao.input_codigo_usuario_2.setText(devolucao.codigo_usuario)
            self.tela_buscar_devolucao.input_data_emprestimo_2.setText(devolucao.data_emprestimo)
        else:
            QMessageBox.information(None, "POO2", "O exemplar ainda não foi devolvido!")

    def botao_Voltar_Buscar_Devolucao(self):  # Método para ativar o botão voltar da tela emprestimo
        self.QtStack.setCurrentIndex(4)


    def botao_Voltar_Biblioteca_Usuario(self):  # Método para ativar o botão voltar da tela emprestimo
        self.usuario = None
        self.QtStack.setCurrentIndex(0)

    @staticmethod
    def botao_sair_login(self):
        client_socket.send('0'.encode())
        client_socket.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())


