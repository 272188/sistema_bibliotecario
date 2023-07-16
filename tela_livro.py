# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_livro.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Livro(object):
    """
    classe que representa a tela de cadastro de livros, sendo esta especifica para o administrador(es) do sistema.

    ...
    Atributes
    ----------
    resize : object
        dimensiona largura e altura da tela
    setStyleSheet : object
        estiliza a cor de fundo da tela
    setObjectName : object
        rotula algum lugar da tela, onde se deseja definir um nome ou frase curta
    setText :
        O método setText() da classe java.text.CollationElementIterator é usado para definir a nova string de origem para o objeto
    QLineEdit : object
        É um campo ou caixa de texto.
    QPushButton : object
        atribuem-se aos botoes de acoes da tela
    botao_cadastrar_livro :
        elemento instanciado do QPushButton, que foi rotulado para identifica-lo como o botao para cadastrar um livro.
    botao_voltar_livro :
        elemento instanciado do QPushButton, que foi rotulado para identifica-lo como o botao para voltar da tela cadastro de livro para a tela principal da biblioteca para administrador(es) do sistema.
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 703)
        MainWindow.setStyleSheet("background-color: rgb(0, 90, 135);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cadastrar_livro = QtWidgets.QLabel(self.centralwidget)
        self.cadastrar_livro.setGeometry(QtCore.QRect(510, 60, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cadastrar_livro.setFont(font)
        self.cadastrar_livro.setObjectName("cadastrar_livro")
        self.codigo_autor = QtWidgets.QLabel(self.centralwidget)
        self.codigo_autor.setGeometry(QtCore.QRect(740, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.codigo_autor.setFont(font)
        self.codigo_autor.setObjectName("codigo_autor")
        self.input_codigo_autor = QtWidgets.QLineEdit(self.centralwidget)
        self.input_codigo_autor.setGeometry(QtCore.QRect(890, 120, 231, 31))
        self.input_codigo_autor.setObjectName("input_codigo_autor")
        self.codigo_livro = QtWidgets.QLabel(self.centralwidget)
        self.codigo_livro.setGeometry(QtCore.QRect(740, 180, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.codigo_livro.setFont(font)
        self.codigo_livro.setObjectName("codigo_livro")
        self.input_codigo_livro = QtWidgets.QLineEdit(self.centralwidget)
        self.input_codigo_livro.setGeometry(QtCore.QRect(890, 170, 231, 31))
        self.input_codigo_livro.setObjectName("input_codigo_livro")
        self.titulo_livro = QtWidgets.QLabel(self.centralwidget)
        self.titulo_livro.setGeometry(QtCore.QRect(30, 180, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.titulo_livro.setFont(font)
        self.titulo_livro.setObjectName("titulo_livro")
        self.input_titulo_livro = QtWidgets.QLineEdit(self.centralwidget)
        self.input_titulo_livro.setGeometry(QtCore.QRect(170, 170, 551, 31))
        self.input_titulo_livro.setObjectName("input_titulo_livro")
        self.editora = QtWidgets.QLabel(self.centralwidget)
        self.editora.setGeometry(QtCore.QRect(30, 280, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.editora.setFont(font)
        self.editora.setObjectName("editora")
        self.input_editora = QtWidgets.QLineEdit(self.centralwidget)
        self.input_editora.setGeometry(QtCore.QRect(170, 270, 291, 31))
        self.input_editora.setObjectName("input_editora")
        self.ano_publicacao = QtWidgets.QLabel(self.centralwidget)
        self.ano_publicacao.setGeometry(QtCore.QRect(480, 330, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ano_publicacao.setFont(font)
        self.ano_publicacao.setObjectName("ano_publicacao")
        self.input_ano_publicacao = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ano_publicacao.setGeometry(QtCore.QRect(630, 320, 261, 31))
        self.input_ano_publicacao.setObjectName("input_ano_publicacao")
        self.isbn = QtWidgets.QLabel(self.centralwidget)
        self.isbn.setGeometry(QtCore.QRect(740, 220, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.isbn.setFont(font)
        self.isbn.setObjectName("isbn")
        self.input_isbn = QtWidgets.QLineEdit(self.centralwidget)
        self.input_isbn.setGeometry(QtCore.QRect(810, 220, 311, 31))
        self.input_isbn.setObjectName("input_isbn")
        self.assunto = QtWidgets.QLabel(self.centralwidget)
        self.assunto.setGeometry(QtCore.QRect(30, 230, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.assunto.setFont(font)
        self.assunto.setObjectName("assunto")
        self.input_assunto = QtWidgets.QLineEdit(self.centralwidget)
        self.input_assunto.setGeometry(QtCore.QRect(170, 220, 551, 31))
        self.input_assunto.setObjectName("input_assunto")
        self.edicao = QtWidgets.QLabel(self.centralwidget)
        self.edicao.setGeometry(QtCore.QRect(480, 270, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.edicao.setFont(font)
        self.edicao.setObjectName("edicao")
        self.input_edicao = QtWidgets.QLineEdit(self.centralwidget)
        self.input_edicao.setGeometry(QtCore.QRect(560, 270, 231, 31))
        self.input_edicao.setObjectName("input_edicao")
        self.num_paginas = QtWidgets.QLabel(self.centralwidget)
        self.num_paginas.setGeometry(QtCore.QRect(30, 330, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.num_paginas.setFont(font)
        self.num_paginas.setObjectName("num_paginas")
        self.volume = QtWidgets.QLabel(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(810, 270, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.volume.setFont(font)
        self.volume.setObjectName("volume")
        self.input_volume = QtWidgets.QLineEdit(self.centralwidget)
        self.input_volume.setGeometry(QtCore.QRect(890, 270, 231, 31))
        self.input_volume.setObjectName("input_volume")
        self.input_num_paginas = QtWidgets.QLineEdit(self.centralwidget)
        self.input_num_paginas.setGeometry(QtCore.QRect(170, 320, 291, 31))
        self.input_num_paginas.setObjectName("input_num_paginas")
        self.botao_cadastrar_livro = QtWidgets.QPushButton(self.centralwidget)
        self.botao_cadastrar_livro.setGeometry(QtCore.QRect(980, 400, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.botao_cadastrar_livro.setFont(font)
        self.botao_cadastrar_livro.setStyleSheet("background-color: rgb(134, 134, 100);")
        self.botao_cadastrar_livro.setObjectName("botao_cadastrar_livro")
        self.nome_autor = QtWidgets.QLabel(self.centralwidget)
        self.nome_autor.setGeometry(QtCore.QRect(30, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.nome_autor.setFont(font)
        self.nome_autor.setObjectName("nome_autor")
        self.input_nome_autor = QtWidgets.QLineEdit(self.centralwidget)
        self.input_nome_autor.setGeometry(QtCore.QRect(170, 120, 551, 31))
        self.input_nome_autor.setObjectName("input_nome_autor")
        self.botao_voltar_livro = QtWidgets.QPushButton(self.centralwidget)
        self.botao_voltar_livro.setGeometry(QtCore.QRect(520, 590, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.botao_voltar_livro.setFont(font)
        self.botao_voltar_livro.setStyleSheet("background-color: rgb(134, 134, 100);")
        self.botao_voltar_livro.setObjectName("botao_voltar_livro")
        self.sistema_bibliotecario = QtWidgets.QLabel(self.centralwidget)
        self.sistema_bibliotecario.setGeometry(QtCore.QRect(410, 10, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sistema_bibliotecario.setFont(font)
        self.sistema_bibliotecario.setObjectName("sistema_bibliotecario")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cadastrar_livro.setText(_translate("MainWindow", "Cadastrar livro"))
        self.codigo_autor.setText(_translate("MainWindow", "Código do autor:"))
        self.codigo_livro.setText(_translate("MainWindow", "Código do livro:"))
        self.titulo_livro.setText(_translate("MainWindow", "Titulo do livro:"))
        self.editora.setText(_translate("MainWindow", "Editora:"))
        self.ano_publicacao.setText(_translate("MainWindow", "Ano publicação:"))
        self.isbn.setText(_translate("MainWindow", "ISBN:"))
        self.assunto.setText(_translate("MainWindow", "Assunto:"))
        self.edicao.setText(_translate("MainWindow", "Edição:"))
        self.num_paginas.setText(_translate("MainWindow", "Nº de páginas:"))
        self.volume.setText(_translate("MainWindow", "Volume:"))
        self.botao_cadastrar_livro.setText(_translate("MainWindow", "Cadastrar"))
        self.nome_autor.setText(_translate("MainWindow", "Nome do autor:"))
        self.botao_voltar_livro.setText(_translate("MainWindow", "Voltar"))
        self.sistema_bibliotecario.setText(_translate("MainWindow", "SISTEMA BIBLIOTECÁRIO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Livro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
