# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_exemplar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Exemplar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1017, 749)
        MainWindow.setStyleSheet("background-color: rgb(0, 90, 135);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cadastrar_exemplar = QtWidgets.QLabel(self.centralwidget)
        self.cadastrar_exemplar.setGeometry(QtCore.QRect(380, 100, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cadastrar_exemplar.setFont(font)
        self.cadastrar_exemplar.setObjectName("cadastrar_exemplar")
        self.codigo_livro = QtWidgets.QLabel(self.centralwidget)
        self.codigo_livro.setGeometry(QtCore.QRect(30, 230, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.codigo_livro.setFont(font)
        self.codigo_livro.setObjectName("codigo_livro")
        self.codigo_exemplar = QtWidgets.QLabel(self.centralwidget)
        self.codigo_exemplar.setGeometry(QtCore.QRect(480, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.codigo_exemplar.setFont(font)
        self.codigo_exemplar.setObjectName("codigo_exemplar")
        self.qtd_dias = QtWidgets.QLabel(self.centralwidget)
        self.qtd_dias.setGeometry(QtCore.QRect(30, 290, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.qtd_dias.setFont(font)
        self.qtd_dias.setObjectName("qtd_dias")
        self.input_codigo_livro = QtWidgets.QLineEdit(self.centralwidget)
        self.input_codigo_livro.setGeometry(QtCore.QRect(180, 230, 281, 31))
        self.input_codigo_livro.setObjectName("input_codigo_livro")
        self.input_codigo_exemplar = QtWidgets.QLineEdit(self.centralwidget)
        self.input_codigo_exemplar.setGeometry(QtCore.QRect(660, 230, 271, 31))
        self.input_codigo_exemplar.setObjectName("input_codigo_exemplar")
        self.botao_cadastrar_exemplar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_cadastrar_exemplar.setGeometry(QtCore.QRect(790, 390, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.botao_cadastrar_exemplar.setFont(font)
        self.botao_cadastrar_exemplar.setStyleSheet("background-color: rgb(134, 134, 100);")
        self.botao_cadastrar_exemplar.setObjectName("botao_cadastrar_exemplar")
        self.input_qtd_dias = QtWidgets.QLineEdit(self.centralwidget)
        self.input_qtd_dias.setGeometry(QtCore.QRect(340, 290, 211, 31))
        self.input_qtd_dias.setObjectName("input_qtd_dias")
        self.sistema_bibliotecario = QtWidgets.QLabel(self.centralwidget)
        self.sistema_bibliotecario.setGeometry(QtCore.QRect(330, 20, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sistema_bibliotecario.setFont(font)
        self.sistema_bibliotecario.setObjectName("sistema_bibliotecario")
        self.botao_voltar_exemplar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_voltar_exemplar.setGeometry(QtCore.QRect(440, 610, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.botao_voltar_exemplar.setFont(font)
        self.botao_voltar_exemplar.setStyleSheet("background-color: rgb(134, 134, 100);")
        self.botao_voltar_exemplar.setObjectName("botao_voltar_exemplar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cadastrar_exemplar.setText(_translate("MainWindow", "Cadastrar exemplar"))
        self.codigo_livro.setText(_translate("MainWindow", "Código do livro:"))
        self.codigo_exemplar.setText(_translate("MainWindow", "Código do exemplar:"))
        self.qtd_dias.setText(_translate("MainWindow", "Quantidade de dias para empréstimo:"))
        self.botao_cadastrar_exemplar.setText(_translate("MainWindow", "Cadastrar"))
        self.sistema_bibliotecario.setText(_translate("MainWindow", "SISTEMA BIBLIOTECÁRIO"))
        self.botao_voltar_exemplar.setText(_translate("MainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Exemplar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())