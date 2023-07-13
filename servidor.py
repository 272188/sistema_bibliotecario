from usuario import Usuario
from biblioteca import Biblioteca
import threading
import socket

import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 8080
addr = (host, port)
bib = Biblioteca()

def menu(con, cliente):

    connected = True
    while connected:

        msg = int(con.recv(1024).decode())
        
        if msg == 0:          #cadastrar usuario
            connected =  False
        
        elif msg  == 1:  #cadastrar usuario

            dados = con.recv(4096).decode()
            lista = dados.split(',')
            usuario = Usuario(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9], lista[10])
            retorno = bib.cadastrarUsuario(usuario)
            

            if(retorno == True):
                con.send('1'.encode())
            elif(retorno == False):
                con.send('0'.encode())

        elif msg == 2:    #realizar login

            dados = con.recv(4096).decode()
            lista_de_login = dados.split(',')

            if(bib.buscarUsuario(lista_de_login[0]) == None):
                con.send('0'.encode())

            else:

                selecionar = bib.verificarLogin(lista_de_login[0],lista_de_login[1])

                if (selecionar != None):

                    verificarLogin = []
                    verificarLogin.append(selecionar.codigo_usuario)
                    verificarLogin.append(selecionar.senha)
                    
                    dados = ",".join(verificarLogin)
                    con.send(dados.encode())
                else:
                    con.send('1'.encode())

        #elif msg == 3:  #buscar usuario

           

       


    print(f"[DESCONECTADO] client: {cliente}")
    con.close()

def main():

    print("[INICIADO] Aguardado conexão...")
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen()

    while True:

        con, cliente = serv_socket.accept()
        print(f"[CONECTADO] client: {cliente}")
        thread = threading.Thread(target=menu, args=(con, cliente))
        thread.start()


def main():

    print("[INICIADO] Aguardado conexão...")
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen()

    while True:

        con, cliente = serv_socket.accept()
        print(f"[CONECTADO] client: {cliente}")
        thread = threading.Thread(target=menu, args=(con, cliente))
        thread.start()

if __name__ == "__main__":
    main()

