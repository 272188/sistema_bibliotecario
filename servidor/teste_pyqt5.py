#Verificar se o PyQt5 foi instalado corretamente
from PyQt5.QtWidgets import QApplication, QLabel   #importando PyQt5
app = QApplication([])
label = QLabel ('Hello world')   #label atribui rótulo de texto informativo
label.show()   #função de mostrar label definida
app.exec_()  #função de executar app