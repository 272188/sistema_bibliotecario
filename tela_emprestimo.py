# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_emprestimo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Emprestimo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 730)
        MainWindow.setStyleSheet("background-color: rgb(72, 145, 218);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.realizar_emprestimo = QtWidgets.QLabel(self.centralwidget)
        self.realizar_emprestimo.setGeometry(QtCore.QRect(470, 100, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.realizar_emprestimo.setFont(font)
        self.realizar_emprestimo.setObjectName("realizar_emprestimo")
        self.codigo_usuario = QtWidgets.QLabel(self.centralwidget)
        self.codigo_usuario.setGeometry(QtCore.QRect(50, 230, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.codigo_usuario.setFont(font)
        self.codigo_usuario.setObjectName("codigo_usuario")
        self.codigo_exemplar = QtWidgets.QLabel(self.centralwidget)
        self.codigo_exemplar.setGeometry(QtCore.QRect(560, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.codigo_exemplar.setFont(font)
        self.codigo_exemplar.setObjectName("codigo_exemplar")
        self.codigo_livro = QtWidgets.QLabel(self.centralwidget)
        self.codigo_livro.setGeometry(QtCore.QRect(50, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.codigo_livro.setFont(font)
        self.codigo_livro.setObjectName("codigo_livro")
        self.data_emprestimo = QtWidgets.QLabel(self.centralwidget)
        self.data_emprestimo.setGeometry(QtCore.QRect(560, 280, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.data_emprestimo.setFont(font)
        self.data_emprestimo.setObjectName("data_emprestimo")
        self.data_devolucao = QtWidgets.QLabel(self.centralwidget)
        self.data_devolucao.setGeometry(QtCore.QRect(50, 330, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.data_devolucao.setFont(font)
        self.data_devolucao.setObjectName("data_devolucao")
        self.input_codigo_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.input_codigo_usuario.setGeometry(QtCore.QRect(210, 230, 321, 31))
        self.input_codigo_usuario.setObjectName("input_codigo_usuario")
        self.input_codigo_exemplar = QtWidgets.QLineEdit(self.centralwidget)
        self.input_codigo_exemplar.setGeometry(QtCore.QRect(740, 230, 321, 31))
        self.input_codigo_exemplar.setObjectName("input_codigo_exemplar")
        self.input_codigo_livro = QtWidgets.QLineEdit(self.centralwidget)
        self.input_codigo_livro.setGeometry(QtCore.QRect(210, 280, 321, 31))
        self.input_codigo_livro.setObjectName("input_codigo_livro")
        self.input_data_emprestimo = QtWidgets.QLineEdit(self.centralwidget)
        self.input_data_emprestimo.setGeometry(QtCore.QRect(740, 280, 321, 31))
        self.input_data_emprestimo.setObjectName("input_data_emprestimo")
        self.input_data_devolucao = QtWidgets.QLineEdit(self.centralwidget)
        self.input_data_devolucao.setGeometry(QtCore.QRect(210, 330, 321, 31))
        self.input_data_devolucao.setObjectName("input_data_devolucao")
        self.botao_realizar_emprestimo = QtWidgets.QPushButton(self.centralwidget)
        self.botao_realizar_emprestimo.setGeometry(QtCore.QRect(920, 380, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.botao_realizar_emprestimo.setFont(font)
        self.botao_realizar_emprestimo.setStyleSheet("background-color: rgb(134, 134, 100);")
        self.botao_realizar_emprestimo.setObjectName("botao_realizar_emprestimo")
        self.botao_voltat_emprestimo = QtWidgets.QPushButton(self.centralwidget)
        self.botao_voltat_emprestimo.setGeometry(QtCore.QRect(570, 750, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.botao_voltat_emprestimo.setFont(font)
        self.botao_voltat_emprestimo.setObjectName("botao_voltat_emprestimo")
        self.sistema_bibliotecario = QtWidgets.QLabel(self.centralwidget)
        self.sistema_bibliotecario.setGeometry(QtCore.QRect(400, 30, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sistema_bibliotecario.setFont(font)
        self.sistema_bibliotecario.setObjectName("sistema_bibliotecario")
        self.botao_voltar_realizar_emprestimo = QtWidgets.QPushButton(self.centralwidget)
        self.botao_voltar_realizar_emprestimo.setGeometry(QtCore.QRect(530, 600, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.botao_voltar_realizar_emprestimo.setFont(font)
        self.botao_voltar_realizar_emprestimo.setStyleSheet("background-color: rgb(134, 134, 100);")
        self.botao_voltar_realizar_emprestimo.setObjectName("botao_voltar_realizar_emprestimo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.realizar_emprestimo.setText(_translate("MainWindow", "Realizar Empréstimo"))
        self.codigo_usuario.setText(_translate("MainWindow", "Código do usuário:"))
        self.codigo_exemplar.setText(_translate("MainWindow", "Código do exemplar:"))
        self.codigo_livro.setText(_translate("MainWindow", "Código do livro:"))
        self.data_emprestimo.setText(_translate("MainWindow", "Data do empréstimo:"))
        self.data_devolucao.setText(_translate("MainWindow", "Data da devolução:"))
        self.botao_realizar_emprestimo.setText(_translate("MainWindow", "Emprestar"))
        self.botao_voltat_emprestimo.setText(_translate("MainWindow", "Voltar"))
        self.sistema_bibliotecario.setText(_translate("MainWindow", "SISTEMA BIBLIOTECÁRIO"))
        self.botao_voltar_realizar_emprestimo.setText(_translate("MainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Emprestimo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
