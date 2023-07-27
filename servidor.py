from usuario import Usuario
from autor import Autor
from livro import Livro
from exemplar import Exemplar
from emprestimo import Emprestimo
from devolucao import Devolucao
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
    """
    Construtor para criar os atributos ao instanciar um objeto. Executa todas condicoes contidas nos demais metodos com conexao entre cliente e servidor 

    Parameters
    ---------
    con : objeto
        conexão da maquina que o usuário está usando 
    cliente : objeto
        endereço da maquina do usuário

    """

    connected = True   #conectado recebe verdadeiro
    while connected:   #enquanto a conexao entre cliente e servidor estiver estabelecida

        msg = int(con.recv(1024).decode())  #msg recebe conexao de informacoes decodificadas
        
        
        if msg == 0:     #se a mensagem for zero significa que nao foi conectado
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
            selecionar = bib.verificarLogin(lista_de_login[0],lista_de_login[1])

            if selecionar == None:
                con.send('0'.encode())
            elif selecionar == False:
                con.send('1'.encode())
            else:
                con.send(f'2,{selecionar.codigo_usuario},{selecionar.nome},{selecionar.cpf},{selecionar.telefone},{selecionar.endereco},{selecionar.bairro},{selecionar.cidade},{selecionar.cep},{selecionar.email},{selecionar.senha},{selecionar.tipo}'.encode())
        
        elif msg == 3:  #buscar usuario
            dados_usuarios = con.recv(4096).decode()
            lista_usuarios = dados_usuarios.split(',')
            verifica = bib.buscarUsuario(lista_usuarios[0])
           
            if verifica != None:
                con.send('0'.encode())
            else:
                con.send('1'.encode())
        
        elif msg == 4: #cadastrar autor
            dados_autor = con.recv(4096).decode()
            lista_autor = dados_autor.split(',')
            autor = Autor(lista_autor[0],lista_autor[1])
            retorno = bib.cadastrarAutor(autor)
            if(retorno == True):
                con.send('1'.encode())
            elif(retorno == False):
                con.send('0'.encode())

        elif msg == 5: #buscar autor
            dados_autores = con.recv(4096).decode()
            lista_autores = dados_autores.split(',')
            verifica = bib.buscarAutores(lista_autores[1])#conferir posicao nome do autor
            if verifica != None:
                con.send('0'.encode())
            else:
                con.send('1'.encode())

        elif msg == 6: #cadastrar livro
            dados_livro = con.recv(4096).decode()
            lista_livro = dados_livro.split(',')
            livro = Livro(lista_livro[0],lista_livro[1],lista_livro[2],lista_livro[3],lista_livro[4],lista_livro[5],lista_livro[6],lista_livro[7],lista_livro[8],lista_livro[9], lista_livro[10])
            retorno = bib.cadastrarLivros(livro)
            if(retorno == True):
                con.send('1'.encode())
            elif(retorno == False):
                con.send('0'.encode())

        elif msg == 7: #buscar livro
            dados_livros = con.recv(4096).decode()
            lista_livros = dados_livros.split(',')
            verifica = bib.buscarLivros(lista_livros[0])
            if verifica != None:
                con.send('0'.encode())
            else:
                con.send('1'.encode())

        elif msg == 8: #cadastrar exemplar
            dados_exemplar = con.recv(4096).decode()
            lista_exemplar = dados_exemplar.split(',')
            exemplar = Exemplar(lista_exemplar [0],lista_exemplar [1],lista_exemplar[2])
            retorno = bib.cadastrarExemplares(exemplar)
            if(retorno == True):
                con.send('1'.encode())
            elif(retorno == False):
                con.send('0'.encode())
        
        #elif msg == 9: #buscar exemplar
        
        elif msg == 10: #realizar emprestimo
            dados_emprestimo = con.recv(4096).decode()
            lista_emprestimo = dados_emprestimo.split(',')
            emprestimo = Emprestimo( lista_emprestimo[0], lista_emprestimo[1], lista_emprestimo[2], lista_emprestimo[3], lista_emprestimo[4])
            retorno = bib.realizarEmprestimo(emprestimo)
            if(retorno == True):
                con.send('1'.encode())
            elif(retorno == False):
                con.send('0'.encode())
        
        #elif msg == 11: #buscar emprestimo

        elif msg == 12:
            dados_devolucao = con.recv(4096).decode()
            lista_devolucao = dados_devolucao.split(',')
            devolucao = Devolucao(lista_devolucao[0],lista_devolucao[1],lista_devolucao[2],lista_devolucao[3],lista_devolucao[4])
            retorno = bib.realizarDevolucao(devolucao)
            if(retorno == True):
                con.send('1'.encode())
            elif(retorno == False):
                con.send('0'.encode())
        
        #elif msg == 13: #buscar devolucao

        
    print(f"[DESCONECTADO] client: {cliente}")
    con.close()

def main():
    """
    Construtor para criar os atributos ao instanciar um objeto. Executa as conexoes entre cliente e sevidor.

    Parameters
    ---------
    socket: object
        envia dados pela rede
    con : object
        conexão da maquina que o usuário está usando 
    cliente : object
        endereço da maquina do usuário
    thread : object
        sequência de instruções do programa que pode ser executada de forma independente.


    """

    print("[INICIADO] Aguardando conexão...")
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

