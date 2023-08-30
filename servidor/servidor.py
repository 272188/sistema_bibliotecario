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
            dados = msg[1:]
            if usuario := bib.cadastrarUsuario(*dados):
                con.send('1'.encode())
                print(f"[CADASTRO REALIZADO] - [{usuario.email}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[CADASTRO FALHOU] client: {cliente}")
        elif msg[0] == '2':
            dados = msg[1:]
            usuario = bib.verificarLogin(*dados)
            if usuario == None:
                con.send('0'.encode())
                print(f"[LOGIN FALHOU] client: {cliente}")
            elif usuario.is_admin:
                con.send('2,1'.encode())
                print(f"[LOGIN ADMIN] - [{bib.usuario.email}] client: {cliente}")
            else:
                con.send('2,0'.encode())
                print(f"[LOGIN USUARIO] - [{bib.usuario.email}] client: {cliente}")
        elif msg[0] == '3':
            pesquisa = msg[1]
            if livros := bib.listarLivros(pesquisa):
                enviar = '3|'
                for livro in livros:
                    enviar += f'{livro}|'
                con.send(enviar.encode())
                print(f"[LISTA LIVROS] - [{bib.usuario.email}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[LISTA LIVROS FALHOU] - [{bib.usuario.email}] client: {cliente}")
        elif msg[0] == '4':
            id_livro = msg[1]
            if bib.realizarEmprestimo(id_livro):
                con.send('4'.encode())
                print(f"[EMPRESTIMO REALIZADO] - [{bib.usuario.email}] - [{bib.buscarLivro(id_livro).titulo}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[EMPRESTIMO FALHOU] - [{bib.usuario.email}] - [{bib.buscarLivro(id_livro).titulo}] client: {cliente}")
        elif msg[0] == '5':
            id_livro = msg[1]
            if bib.realizarDevolucao(id_livro):
                con.send('5'.encode())
                print(f"[DEVOLUCAO REALIZADA] - [{bib.usuario.email}] - [{bib.buscarLivro(id_livro).titulo}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[DEVOLUCAO FALHOU] - [{bib.usuario.email}] - [{bib.buscarLivro(msg[1]).titulo}] client: {cliente}")
        elif msg[0] == '6':
            enviar = '6|'
            for emp in bib.listarEmprestimos():
                enviar += f'{str(bib.buscarLivro(emp.id_livro))[:-2]},{emp.data_emprestimo},{emp.data_devolucao}|'
            con.send(enviar.encode())
        elif msg[0] == '7':
            email = msg[1]
            if bib.excluirUsuario(email):
                con.send('7'.encode())
                print(f"[USUARIO EXCLUIDO] - [{bib.usuario.email}] - [{email}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[USUARIO NAO EXCLUIDO] - [{bib.usuario.email}] - [{email}] client: {cliente}")
        elif msg[0] == '8':
            enviar = '8|'
            for usuario in bib.listarUsuarios():
                enviar += f'{usuario}|'
            con.send(enviar.encode())
        elif msg[0] == '9':
            dados = msg[1:]
            bib.cadastrarLivros(*dados)
            con.send('9'.encode())
            print(f"[LIVRO CADASTRADO] - [{bib.usuario.email}] client: {cliente}")
        elif msg[0] == '10':
            id_livro = msg[1]
            if bib.excluirLivro(id_livro):
                con.send('10'.encode())
                print(f"[LIVRO EXCLUIDO] - [{bib.usuario.email}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[LIVRO NAO EXCLUIDO] - [{bib.usuario.email}] client: {cliente}")
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
