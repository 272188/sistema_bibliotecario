#importação das classes
from pessoa import Pessoa
from usuario import Usuario
from autor import Autor
from livro import Livro
from exemplar import Exemplar
from emprestimo import Emprestimo
from devolucao import Devolucao

from datetime import date

#importação do banco de dados
import mysql.connector 


class Biblioteca:
    __slots__ = ['conexao','cursor','mysql']
    def __init__(self):
        #configuração da conexão com banco de dados
        self.conexao = mysql.connector.connect(host = 'localhost', user = 'sheila', password= 'root', database = 'banco_bib')
        self.cursor = self.conexao.cursor()
        self.mysql = """CREATE TABLE IF NOT EXISTS pessoa(nome VARCHAR(20) NOT NULL PRIMARY KEY, sobrenome VARCHAR(40) NOT NULL)"""

        self.cursor.execute(self.mysql)
        self.conexao.commit()

        self.mysql = """CREATE TABLE IF NOT EXISTS usuario(codigo_usuario varchar(30) NOT NULL PRIMARY KEY, nome VARCHAR(45) NOT NULL, cpf VARCHAR(14) NOT NULL, telefone VARCHAR(20) NOT NULL, endereco VARCHAR(60) NOT NULL, bairro VARCHAR(45) NOT NULL, cidade VARCHAR(45) NOT NULL, cep VARCHAR(20) NOT NULL, email VARCHAR(40) NOT NULL, senha VARCHAR(20) NOT NULL, tipo VARCHAR(20) NOT NULL DEFAULT 'usuario')"""

        self.cursor.execute(self.mysql)
        self.conexao.commit()


        self.mysql = """CREATE TABLE IF NOT EXISTS autor(codigo_autor varchar(30) NOT NULL PRIMARY KEY, nome_autor VARCHAR(45) NOT NULL)"""

        self.cursor.execute(self.mysql)
        self.conexao.commit()


        self.mysql = """CREATE TABLE IF NOT EXISTS livro(codigo_livro varchar(30) NOT NULL PRIMARY KEY, nome_autor VARCHAR(45) NOT NULL, codigo_autor varchar(30) NOT NULL, titulo VARCHAR(200) NOT NULL, editora VARCHAR(45) NOT NULL, isbn VARCHAR(20) NOT NULL, assunto VARCHAR(100) NOT NULL, edicao varchar(30) NOT NULL, volume varchar(30) NOT NULL, Numero_pag varchar(30) NOT NULL, anoPublicacao varchar(30) NOT NULL)"""

        self.cursor.execute(self.mysql)
        self.conexao.commit()

        self.mysql = """CREATE TABLE IF NOT EXISTS exemplar(codigo_exemplar varchar(30) NOT NULL PRIMARY KEY, codigo_livro varchar(30) NOT NULL, dias_emprestimo varchar(30) NOT NULL)"""

        self.cursor.execute(self.mysql)
        self.conexao.commit()

        self.mysql = """CREATE TABLE IF NOT EXISTS emprestimo(codigo_usuario varchar(30) NOT NULL PRIMARY KEY, codigo_livro varchar(30) NOT NULL, codigo_exemplar varchar(30) NOT NULL, data_emprestimo VARCHAR(10) NOT NULL, data_para_devolver VARCHAR(10) NOT NULL)"""
        self.cursor.execute(self.mysql)
        self.conexao.commit()

        self.mysql = """CREATE TABLE IF NOT EXISTS devolucao(codigo_usuario varchar(30) NOT NULL PRIMARY KEY, codigo_livro varchar(30) NOT NULL, codigo_exemplar varchar(30) NOT NULL, data_emprestimo VARCHAR(10) NOT NULL, data_devolucao VARCHAR(10) NOT NULL)"""
        
        self.cursor.execute(self.mysql)
        self.conexao.commit()
        

    def verificarLogin(self, codigo_usuario, senha):

        selecionar = self.buscarUsuario(codigo_usuario)
            
        if(senha == selecionar.senha):

            return selecionar
        else:
            return None

    def cadastrarUsuario(self, usuario): 
        verifica = self.buscarUsuario(usuario.codigo_usuario)
        if verifica == None:
            self.cursor.execute('INSERT INTO usuario(codigo_usuario, nome, cpf, telefone, endereco, bairro, cidade, cep, email, senha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (usuario.codigo_usuario, usuario.nome, usuario.cpf, usuario.telefone, usuario.endereco, usuario.bairro, usuario.cidade, usuario.cep, usuario.email, usuario.senha))
            self.conexao.commit()
            return True
        else:
            return False

        
    def buscarUsuario(self, codigo_usuario): #-> Usuario | None:
        self.cursor.execute("SELECT * FROM usuario WHERE codigo_usuario = %s", (codigo_usuario,))
        selecionar = self.cursor.fetchone()
        if (selecionar == None):
            return None
        else:
            usuario = Usuario(selecionar[0],selecionar[1],selecionar[2],selecionar[3],selecionar[4],selecionar[5],selecionar[6],selecionar[7],selecionar[8],selecionar[9],selecionar[10])
            return usuario
    
    def cadastrarAutor(self, autor):
        verifica = self.buscarAutores(autor.nome_autor)
        if verifica == None:
            self.cursor.execute('INSERT INTO autor(codigo_autor, nome_autor) VALUES(%s, %s)', (autor.codigo_autor, autor.nome_autor))
            self.conexao.commit()
            return True
        else:
            return False

    def buscarAutores(self, nome_autor):
        
        self.cursor.execute("SELECT * FROM autor WHERE nome_autor = %s", (nome_autor,))
        selecionar = self.cursor.fetchone()
        # verifica se o autor já foi cadastrado pelo código
        if (selecionar == None):
            return None
        else:
            autor = Autor(selecionar[0],selecionar[1])
            return autor
    
    '''def buscarAutores(self, codigo_autor):
        self.cursor.execute("SELECT * FROM autor WHERE codigo_autor = %s", (codigo_autor,))
        selecionar = self.cursor.fetchone()
        # verifica se o autor já foi cadastrado pelo código
        for autor in selecionar:
            if autor == codigo_autor:
                return autor
        else:
            None'''

    def cadastrarLivros(self, livro):
        verifica = self.buscarLivros(livro.codigo_livro)
        if verifica == None:
            self.cursor.execute('INSERT INTO livro(codigo_livro, nome_autor, codigo_autor, titulo, editora, isbn, assunto, edicao, volume, Numero_pag, anoPublicacao) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (livro.codigo_livro, livro.nome_autor, livro.codigo_autor, livro.titulo, livro.editora, livro.isbn, livro.assunto, livro.edicao, livro.volume, livro.Numero_pag, livro.anoPublicacao))
            self.conexao.commit()
            return True
        else:
            return False

    def buscarLivros(self, codigo_livro):
        self.cursor.execute("SELECT * FROM livro WHERE codigo_livro = %s", (codigo_livro,))
        selecionar = self.cursor.fetchone()
        if (selecionar == None):  # verifica se existe livro cadastrado
            return None
        else:
            livro = Livro(selecionar[0],selecionar[1],selecionar[2],selecionar[3],selecionar[4],selecionar[5],selecionar[6],selecionar[7],selecionar[8],selecionar[9], selecionar[10])
            return livro

    def cadastrarExemplares(self, exemplar):
        verifica = self.buscarExemplares(exemplar.codigo_exemplar)
        if verifica == None:
            self.cursor.execute('INSERT INTO exemplar(codigo_exemplar, codigo_livro, dias_emprestimo) VALUES(%s, %s, %s)', (exemplar.codigo_exemplar, exemplar.codigo_livro, exemplar.dias_emprestimo))
            self.conexao.commit()
            return True
        else:
            return False

    def buscarExemplares(self, codigo_exemplar): 
        self.cursor.execute("SELECT * FROM exemplar WHERE codigo_exemplar = %s", (codigo_exemplar,))
        selecionar = self.cursor.fetchone()
        if (selecionar == None):  
            return None  
        else:
            exemplar = Exemplar(selecionar[0],selecionar[1],selecionar[2])
            return exemplar

    def realizarEmprestimo(self, emprestimo):
        verifica = self.buscarEmprestimo(emprestimo.codigo_exemplar)
        if verifica == None:
            self.cursor.execute('INSERT INTO emprestimo(codigo_usuario, codigo_livro, codigo_exemplar, data_emprestimo, data_para_devolver) VALUES(%s, %s, %s, %s, %s)', (emprestimo.codigo_usuario, emprestimo.codigo_livro, emprestimo.codigo_exemplar, emprestimo.data_emprestimo, emprestimo.data_para_devolver))
            #self.cursor.execute('DELETE FROM exemplar WHERE codigo_exemplar = %s', (exemplar.codigo_exemplar,))
            self.conexao.commit()
            return True
        else:
            return False

    def buscarEmprestimo(self, codigo_exemplar): 
        self.cursor.execute("SELECT * FROM emprestimo WHERE codigo_exemplar = %s", (codigo_exemplar,))
        selecionar = self.cursor.fetchone()
        if (selecionar == None):
            return None
        else:
            emprestimo = Emprestimo(selecionar[0],selecionar[1],selecionar[2],selecionar[3],selecionar[4])
            return emprestimo

    #def removerExemplar(self, codigo_exemplar):
    #    if self.buscarEmprestimo(codigo_exemplar) != None:
    #        self.cursor.execute("DELETE FROM emprestimo WHERE codigo_exemplar = %s", (codigo_exemplar,))
    #        self.conexao.commit()
    #    else:
    #        print("Livre não pode ser removido pois, está em emprestimo")

    def realizarDevolucao(self, devolucao):
        verifica = self.buscarDevolucoes(devolucao.codigo_exemplar, devolucao.data_devolucao)
        if verifica == None:
            self.cursor.execute('INSERT INTO devolucao(codigo_usuario, codigo_livro, codigo_exemplar, data_emprestimo, data_devolucao) VALUES(%s, %s, %s, %s, %s)', (devolucao.codigo_usuario, devolucao.codigo_livro, devolucao.codigo_exemplar, devolucao.data_emprestimo, devolucao.data_devolucao))
            self.conexao.commit()
            return True
        else:
            False

    def buscarDevolucoes(self, codigo_exemplar, data_devolucao):
        self.cursor.execute("SELECT * FROM devolucao WHERE codigo_exemplar = %s AND data_devolucao = %s", (codigo_exemplar, data_devolucao,))
        selecionar = self.cursor.fetchone()
        if (selecionar == None):
            return None
        else:
            devolucao = Devolucao(selecionar[0],selecionar[1],selecionar[2],selecionar[3],selecionar[4])
            return devolucao
        
    '''def Devolucao(self, codigo_exemplar):
        if (verifica = self.buscarEmprestimo(codigo_exemplar)) == True:
            self.cursor.execute("DELETE * FROM emprestimo WHERE codigo_exemplar = %s", (codigo_exemplar,))
            self.conexao.commit()
        else:
            print("O exemplar não possui registro de emprestimo para devolução!")
 

    # def Devolucao(self, codigo_exemplar):
    #     if self.verificarLogin(codigo_usuario, senha):
    #         cursor = self.conexao.cursor()
    #         cursor.execute ("DELETE FROM emprestimos WHERE codigo_exemplar=?", (codigo_exemplar,))
    #         self.conexao.commit()
    #         print("Devolução realizada com sucesso!")
    #     else:
    #         print("Login necessário para realizar a devolução.")



    @property
    def mostraAutores(self):
        if len(self.__autores) > 0:
            for i in self.__autores:
                print(f"Nome: {i.nome} Codigo: {i.codigo}")
        else:
            print("Sem autores cadastrados!")

    # codigo, titulo, editora, int anoPublicacao, ISBN, assunto, edicao, int Numero_pag, volume
    
    
    def mostraLivros(self):
        if len(self.__livros) > 0:
            for i in self.__livros:
                print("codigo: ", i.codigo)
                print("titulo: ", i.titulo)
                print("editora: ", i.editora)
                print("ano de publicação: ", i.anoPublicacao)
                print("ISBN: ", i.ISBN)
                print("assunto: ", i.assunto)
                print("edição: ", i.edicao)
                print("volume: ", i.volume)
                print("número de página: ", i.numero_pag)
        else:
            print("Sem livros cadastrados")

    @property
    def mostraExemplares(self):
        if len(self.__exemplares) > 0:
            for i in self.__exemplares:
                print("código do livro: 1", i.codigo_livro)
                print("código do exemplar: ", i.codigo_exemplar)
                print("dias de empréstimo: ", i.dias_emprestimo)
        else:
            print("Sem exemplares cadastrados!")


# configurações da conexão com o banco de dados
        self.connection = mysql.connect(
            user="root",
            password="root",
            host="localhost",
            database="bd_biblioteca",)
        # conectar com o banco de dados

    conexao = mysql.connect()
    print("Conexão realizada com sucesso!")

    # criando cursor para executar consultas
    cursor = conexao.cursor()

    self.connection = self.create_connection()
        self.cursor = self.connection.cursor() 
        
    def create_connection(self):
        Cria uma conexão com o banco de dados MySQL.

        Returns:
            obj: Objeto de conexão com o banco de dados.
        try:
            
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def close_connection(self):
        Fecha a conexão com o banco de dados.
        if self.connection:
            self.connection.commit()
            self.connection.close()

    # criando cursor para executar consultas


def create_connection(self):
        Cria uma conexão com o banco de dados MySQL.

        Returns:
            obj: Objeto de conexão com o banco de dados.
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='C0mpL3xP@$$',
                database='project_tarefa',
            )
            return connection
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def close_connection(self):
        #Fecha a conexão com o banco de dados.

        if self.connection:
            self.connection.commit()
            self.connection.close()

    cursor = conexao.cursor()  '''