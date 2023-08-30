from modelos import Usuario
from biblioteca import Biblioteca
import threading
import socket


host = socket.gethostbyname(socket.gethostname())
port = 8080
addr = (host, port)


def menu(con: socket.socket, cliente: tuple):
    connected = True
    bib = Biblioteca()
    while connected:
        msg = con.recv(1024).decode().split(',')
        if msg[0] == '0':
            bib.fazerLogout()
            print(f"[LOGOUT] client: {cliente}")
        elif msg[0]  == '1':
            dados = con.recv(4096).decode()
            lista = dados.split(',')
            usuario = Usuario(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9], lista[10])
            retorno = bib.cadastrarUsuario(usuario)
            if(retorno == True):
                con.send('1'.encode())
            elif(retorno == False):
                con.send('0'.encode())
        elif msg[0] == '2':
            dados = msg[1:]
            logado = bib.verificarLogin(*dados)
            if logado == None:
                con.send('0'.encode())
                print(f"[LOGIN FALHOU] client: {cliente}")
            else:
                enviar = '2|'
                for emp in bib.listarEmprestimos():
                    enviar += f'{str(bib.buscarLivro(emp.id_livro))[:-2]},{emp.data_emprestimo},{emp.data_devolucao}|'
                con.send(enviar.encode())
                print(f"[LOGIN COM SUCESSO] - [{bib.usuario.email}] client: {cliente}")
        elif msg[0] == '-1':
            connected = False
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


if __name__ == "__main__":
    main()
