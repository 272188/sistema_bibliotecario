# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/tela_livro.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Livro(object):
    def setupUi(self, Livro):
        Livro.setObjectName("Livro")
        Livro.resize(500, 300)
        Livro.setMinimumSize(QtCore.QSize(500, 300))
        Livro.setMaximumSize(QtCore.QSize(500, 300))
        qtRectangle = Livro.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        Livro.move(qtRectangle.topLeft())
        self.gridLayoutWidget = QtWidgets.QWidget(Livro)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 120, 481, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.caixa_titulo = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.caixa_titulo.setObjectName("caixa_titulo")
        self.gridLayout.addWidget(self.caixa_titulo, 1, 0, 1, 1)
        self.caixa_editora = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.caixa_editora.setObjectName("caixa_editora")
        self.gridLayout.addWidget(self.caixa_editora, 2, 0, 1, 1)
        self.caixa_autor = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.caixa_autor.setObjectName("caixa_autor")
        self.gridLayout.addWidget(self.caixa_autor, 0, 0, 1, 1)
        self.caixa_isbn = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.caixa_isbn.setObjectName("caixa_isbn")
        self.gridLayout.addWidget(self.caixa_isbn, 3, 0, 1, 1)
        self.caixa_edicao = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.caixa_edicao.setObjectName("caixa_edicao")
        self.gridLayout.addWidget(self.caixa_edicao, 0, 1, 1, 1)
        self.caixa_volume = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.caixa_volume.setObjectName("caixa_volume")
        self.gridLayout.addWidget(self.caixa_volume, 1, 1, 1, 1)
        self.caixa_paginas = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.caixa_paginas.setObjectName("caixa_paginas")
        self.gridLayout.addWidget(self.caixa_paginas, 2, 1, 1, 1)
        self.caixa_ano = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.caixa_ano.setObjectName("caixa_ano")
        self.gridLayout.addWidget(self.caixa_ano, 3, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Livro)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 260, 481, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botao_voltar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.botao_voltar.setObjectName("botao_voltar")
        self.horizontalLayout.addWidget(self.botao_voltar)
        self.botao_confirmar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.botao_confirmar.setObjectName("botao_confirmar")
        self.horizontalLayout.addWidget(self.botao_confirmar)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Livro)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 481, 100))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imagem_livros = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.imagem_livros.setMinimumSize(QtCore.QSize(96, 96))
        self.imagem_livros.setMaximumSize(QtCore.QSize(96, 96))
        self.imagem_livros.setTextFormat(QtCore.Qt.AutoText)
        self.imagem_livros.setObjectName("imagem_livros")
        self.horizontalLayout_2.addWidget(self.imagem_livros)

        self.retranslateUi(Livro)
        QtCore.QMetaObject.connectSlotsByName(Livro)

    def retranslateUi(self, Livro):
        _translate = QtCore.QCoreApplication.translate
        Livro.setWindowTitle(_translate("Livro", "Cadastro de Livros"))
        self.caixa_titulo.setPlaceholderText(_translate("Livro", "Título"))
        self.caixa_editora.setPlaceholderText(_translate("Livro", "Editora"))
        self.caixa_autor.setPlaceholderText(_translate("Livro", "Autor"))
        self.caixa_isbn.setPlaceholderText(_translate("Livro", "ISBN"))
        self.caixa_edicao.setPlaceholderText(_translate("Livro", "Edição"))
        self.caixa_volume.setPlaceholderText(_translate("Livro", "Volume"))
        self.caixa_paginas.setPlaceholderText(_translate("Livro", "Páginas"))
        self.caixa_ano.setPlaceholderText(_translate("Livro", "Ano"))
        self.botao_voltar.setText(_translate("Livro", "Voltar"))
        self.botao_confirmar.setText(_translate("Livro", "Confirmar Adição"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Livro = QtWidgets.QWidget()
    ui = Ui_Livro()
    ui.setupUi(Livro)
    Livro.show()
    sys.exit(app.exec_())
