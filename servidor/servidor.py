from modelos import Usuario
from biblioteca import Biblioteca
import threading
import socket


host = socket.gethostbyname(socket.gethostname())
port = 8080
addr = (host, port)


def menu(con: socket.socket, cliente: tuple):
    """
    Este método implementa o menu de interação com o cliente. Ele utiliza um loop para continuar recebendo mensagens do cliente e
    executando as ações correspondentes até que a conexão seja encerrada.

    Parâmetros:
    -----------
    con (socket.socket):
        O socket de conexão com o cliente.
    cliente (tuple):
        A tupla contendo o endereço IP e o número da porta do cliente.

    """
    connected = True  # Define a flag para manter o loop ativo.
    bib = Biblioteca()  # Cria uma instância da classe Biblioteca para interação.
    while connected:
        msg = con.recv(1024).decode().split(',')  # Recebe e decodifica a mensagem do cliente.
        if msg[0] == '0':
            bib.fazerLogout()  # Realiza o logout do usuário.
            print(f"[LOGOUT] client: {cliente}")
        elif msg[0]  == '1': # Realiza cadastro do usuário.
            dados = msg[1:]
            if usuario := bib.cadastrarUsuario(*dados):
                con.send('1'.encode())
                print(f"[CADASTRO REALIZADO] - [{usuario.email}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[CADASTRO FALHOU] client: {cliente}")
        elif msg[0] == '2': # Verifica dados de login do usuário cadastrado e loga-o no sistema.
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
        elif msg[0] == '3': #Lista os livros disponíveis na biblioteca que correspondem à pesquisa feita pelo usuario.
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
        elif msg[0] == '4': #Realiza um empréstimo de um livro para o usuário atual.
            id_livro = msg[1]
            if bib.realizarEmprestimo(id_livro):
                con.send('4'.encode())
                print(f"[EMPRESTIMO REALIZADO] - [{bib.usuario.email}] - [{bib.buscarLivro(id_livro).titulo}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[EMPRESTIMO FALHOU] - [{bib.usuario.email}] - [{bib.buscarLivro(id_livro).titulo}] client: {cliente}")
        elif msg[0] == '5': #Realiza a devolução de um livro previamente emprestado.
            id_livro = msg[1]
            if bib.realizarDevolucao(id_livro):
                con.send('5'.encode())
                print(f"[DEVOLUCAO REALIZADA] - [{bib.usuario.email}] - [{bib.buscarLivro(id_livro).titulo}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[DEVOLUCAO FALHOU] - [{bib.usuario.email}] - [{bib.buscarLivro(msg[1]).titulo}] client: {cliente}")
        elif msg[0] == '6':  #Lista os empréstimos realizados pelo usuário atual.
            enviar = '6|'
            for emp in bib.listarEmprestimos():
                enviar += f'{str(bib.buscarLivro(emp.id_livro))[:-2]},{emp.data_emprestimo},{emp.data_devolucao}|'
            con.send(enviar.encode())
        elif msg[0] == '7': #Exclui um usuário da biblioteca com base no email fornecido.
            email = msg[1]
            if bib.excluirUsuario(email):
                con.send('7'.encode())
                print(f"[USUARIO EXCLUIDO] - [{bib.usuario.email}] - [{email}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[USUARIO NAO EXCLUIDO] - [{bib.usuario.email}] - [{email}] client: {cliente}")
        elif msg[0] == '8': #Lista todos os usuários cadastrados na biblioteca.
            enviar = '8|'
            for usuario in bib.listarUsuarios():
                enviar += f'{usuario}|'
            con.send(enviar.encode())
        elif msg[0] == '9':  #Cadastra um livro na biblioteca com base nos dados fornecidos. 
            dados = msg[1:]
            bib.cadastrarLivros(*dados)
            con.send('9'.encode())
            print(f"[LIVRO CADASTRADO] - [{bib.usuario.email}] client: {cliente}")
        elif msg[0] == '10':  #Exclui um livro da biblioteca com base no ID do livro fornecido.
            id_livro = msg[1]
            if bib.excluirLivro(id_livro):
                con.send('10'.encode())
                print(f"[LIVRO EXCLUIDO] - [{bib.usuario.email}] client: {cliente}")
            else:
                con.send('0'.encode())
                print(f"[LIVRO NAO EXCLUIDO] - [{bib.usuario.email}] client: {cliente}")
        elif msg[0] == '-1': #Encerra a conexão com o cliente e fecha o banco de dados.
            bib.fechar_bd()
            connected = False
    print(f"[DESCONECTADO] client: {cliente}")
    con.close()  # Fecha o socket de conexão quando o loop for encerrado.


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
