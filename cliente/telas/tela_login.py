# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 706)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bemvindo = QtWidgets.QLabel(self.centralwidget)
        self.bemvindo.setGeometry(QtCore.QRect(270, 20, 581, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bemvindo.setFont(font)
        self.bemvindo.setObjectName("bemvindo")
        self.usuario = QtWidgets.QLabel(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(70, 220, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.usuario.setFont(font)
        self.usuario.setObjectName("usuario")
        self.senha = QtWidgets.QLabel(self.centralwidget)
        self.senha.setGeometry(QtCore.QRect(70, 290, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.senha.setFont(font)
        self.senha.setObjectName("senha")
        self.input_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.input_usuario.setGeometry(QtCore.QRect(160, 210, 371, 41))
        self.input_usuario.setObjectName("input_usuario")
        self.input_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.input_senha.setGeometry(QtCore.QRect(160, 280, 371, 41))
        self.input_senha.setObjectName("input_senha")
        self.botao_login = QtWidgets.QPushButton(self.centralwidget)
        self.botao_login.setGeometry(QtCore.QRect(680, 230, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.botao_login.setFont(font)
        self.botao_login.setStyleSheet("background-color: rgb(134, 134, 100);")
        self.botao_login.setObjectName("botao_login")
        self.botao_sair_login = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair_login.setGeometry(QtCore.QRect(940, 600, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.botao_sair_login.setFont(font)
        self.botao_sair_login.setStyleSheet("background-color: rgb(134, 134, 100);")
        self.botao_sair_login.setObjectName("botao_sair_login")
        self.login_2 = QtWidgets.QLabel(self.centralwidget)
        self.login_2.setGeometry(QtCore.QRect(560, 90, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.login_2.setFont(font)
        self.login_2.setObjectName("login_2")
        self.botao_cadastro_login = QtWidgets.QPushButton(self.centralwidget)
        self.botao_cadastro_login.setGeometry(QtCore.QRect(250, 430, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.botao_cadastro_login.setFont(font)
        self.botao_cadastro_login.setStyleSheet("background-color: rgb(134, 134, 100);")
        self.botao_cadastro_login.setObjectName("botao_cadastro_login")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bemvindo.setText(_translate("MainWindow", "BEMVINDO AO SISTEMA BIBLIOTECÁRIO"))
        self.usuario.setText(_translate("MainWindow", "Usuário:"))
        self.senha.setText(_translate("MainWindow", "Senha:"))
        self.botao_login.setText(_translate("MainWindow", "Login"))
        self.botao_sair_login.setText(_translate("MainWindow", "Sair"))
        self.login_2.setText(_translate("MainWindow", "Login"))
        self.botao_cadastro_login.setText(_translate("MainWindow", "Cadastro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())