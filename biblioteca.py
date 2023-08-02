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
    """

	A classe principal, que faz a conexao com banco de dados e cria todas as tabelas, tambem foi utilizada para representar os principais metodos de funcionalidades do sistema

    ...

    Attributes
    ----------
    self.conexao : object
        realiza a conexao entre a classe biblioteca  com o banco de dados, que requer os parametros de acesso e conexao
    self.cursor : object
        cursor mysql que permite executar comandos no banco de dados, será usado sempre que for necessário solicitar algo ao banco de dados 
    
     Methods
    -------
    verificarLogin(codigo_usuario, senha):
        verfifica se o codigo do usuario e a senha corresponde a algum usuario cadastrado no sistema
    cadastrarUsuario(usuario):
        cadastra um usuario se o mesmo nao possuir cadastro
    buscarUsuario(codigo_usuario):
        faz uma busca entre os usuarios cadastrados na tabela de usuario, atraves do codigo de usuario informado
    cadastrarAutor(autor):
        cadastra um autor se o mesmo nao possuir cadastro no sistema
    buscarAutores(nome_autor):
        faz uma busca entre nomes de autores cadastrados na tabela de autor, pelo nome do autor informado
    cadastrarLivros(livro):
        cadastra um livro se o mesmo nao possuir cadastro no sistema
    buscarLivros(codigo_livro):
        faz uma busca entre entre os livros cadastrados na tabela de livro, atraves do codigo do livro informado
    cadastrarExemplares(exemplar):
        cadastra um exemplar de um livro se o mesmo nao possuir cadastro no sistema
    buscarExemplares(codigo_exemplar):
        faz uma busca entre entre os exemplares cadastrados na tabela de exemplar, atraves do codigo do livro informado
    realizarEmprestimo(self, emprestimo):
        cadastra um emprestimo de um exemplar de um livro se o mesmo nao possuir emprestimo no sistema
    buscarEmprestimo(codigo_exemplar):
        faz uma busca entre entre os emprestimos realizados na tabela de emprestimo, atraves do codigo do exemplar informado
    realizarDevolucao(devolucao):
        cadastra a devolucao de um exemplar de um livro se o mesmo possuir emprestimo no sistema
    buscarDevolucoes(codigo_exemplar, data_devolucao):
        faz uma busca entre entre as devolucoes realizadas na tabela de devolucao, atraves do codigo do exemplar e a data da devolucao informada
	"""
   
    __slots__ = ['conexao','cursor','mysql']
    def __init__(self):
        """
        construtor que cria tres atributos referentes ao banco de dados

        Parameters
        ----------

        self.conexao : object
            conexão entre a classe biblioteca com o banco de dados escolhido, onde a mesma precisa dos parametros de acesso e conexão
        self.cursor : object
            cursor mysql que permite executar comandos no banco de dados, será usado sempre que for necessário solicitar algo ao banco de dados
        self.mysql : object
            criar o banco de dados e suas respectivas tabelas caso os mesmos não exista
        """
        #configuração para conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'sheila',
            password= 'root',
            database='banco_bib',
        )
        self.cursor = self.conexao.cursor()
        self.mysql = """CREATE DATABASE IF NOT EXISTS banco_bib"""
        self.cursor.execute(self.mysql) #funcao para executar a acao no mysql
        self.conexao.commit() #Por padrão, não é efetuado commit automaticamente, deve-se commitar para salvar as alteracoes no banco.

        self.mysql = """USE banco_bib"""
        self.cursor.execute(self.mysql)
        self.conexao.commit()
        
        self.mysql = """CREATE TABLE IF NOT EXISTS pessoa(nome VARCHAR(20) NOT NULL PRIMARY KEY, sobrenome VARCHAR(40) NOT NULL)"""

        self.cursor.execute(self.mysql)
        self.conexao.commit()

        self.mysql = """CREATE TABLE IF NOT EXISTS usuario(codigo_usuario varchar(30) NOT NULL PRIMARY KEY, nome VARCHAR(100) NOT NULL, cpf VARCHAR(14) NOT NULL, telefone VARCHAR(20) NOT NULL, endereco VARCHAR(200) NOT NULL, bairro VARCHAR(100) NOT NULL, cidade VARCHAR(100) NOT NULL, cep VARCHAR(20) NOT NULL, email VARCHAR(100) NOT NULL, senha VARCHAR(30) NOT NULL, tipo VARCHAR(20) NOT NULL DEFAULT 'usuario')"""

        self.cursor.execute(self.mysql)
        self.conexao.commit()


        self.mysql = """CREATE TABLE IF NOT EXISTS livro(codigo_livro varchar(30) NOT NULL PRIMARY KEY, nome_autor VARCHAR(45) NOT NULL, codigo_autor varchar(30) NOT NULL, titulo VARCHAR(200) NOT NULL, editora VARCHAR(45) NOT NULL, isbn VARCHAR(20) NOT NULL, assunto VARCHAR(100) NOT NULL, edicao varchar(30) NOT NULL, volume varchar(30) NOT NULL, Numero_pag varchar(30) NOT NULL, anoPublicacao varchar(30) NOT NULL, quantidade_exemplares int NOT NULL)"""

        self.cursor.execute(self.mysql)
        self.conexao.commit()

        self.mysql = """CREATE TABLE IF NOT EXISTS exemplar(codigo_exemplar varchar(30) NOT NULL PRIMARY KEY, codigo_livro varchar(30) NOT NULL, dias_emprestimo varchar(30) NOT NULL)"""

        self.cursor.execute(self.mysql)
        self.conexao.commit()

        self.mysql = """CREATE TABLE IF NOT EXISTS emprestimo(codigo_livro varchar(30) NOT NULL, codigo_exemplar varchar(30) NOT NULL, data_emprestimo VARCHAR(10) NOT NULL, data_para_devolver VARCHAR(10) NOT NULL)"""
        self.cursor.execute(self.mysql)
        self.conexao.commit()

        self.mysql = """CREATE TABLE IF NOT EXISTS devolucao(codigo_usuario varchar(30) NOT NULL PRIMARY KEY, codigo_livro varchar(30) NOT NULL, codigo_exemplar varchar(30) NOT NULL, data_emprestimo VARCHAR(10) NOT NULL, data_devolucao VARCHAR(10) NOT NULL)"""
        
        self.cursor.execute(self.mysql)
        self.conexao.commit()
        

    def verificarLogin(self, codigo_usuario, senha):
        """
        verifica se o codigo do usuario e senha informado corresponde aos dos usuarios ja cadastrados no sistema e assim, permitir logar no sistema.

        Parameters
        ----------
        codigo_usuario {string}:
            codigo de identificao do usuario que podera conter numero e/ou caracteres especiais ao se cadastrar
        senha {string} :
            hash da senha em formato de string para garatir a seguranca no acesso ao sistema
        return {boolean}: 
            Boleano referente ao resultado para retorno das condicoes das funcoes
        """

        selecionar = self.buscarUsuario(codigo_usuario) #selecionar recebe a funcao buscarUsuario, que busca o usuario por seu codigo cadastrado
            
        if selecionar == None:
            return None
        elif selecionar.senha != senha:
            return False
        else:
            return selecionar

    def cadastrarUsuario(self, usuario):
        """
        verifica se o codigo do usuario informado corresponde aos dos usuarios ja cadastrados no sistema, caso nao, realiza um novo cadastro de usuario

        Parameters
        ----------
        codigo_usuario {string}:
            codigo de identificao do usuario em formato de string, que podera conter numero e/ou caracteres especiais ao se cadastrar
        return {boolean}: 
            referente ao retorno com o resultado em formato Boleano (verdadeiro ou falso) das condicoes das funcoes
        VALUES:
            refere-se formato de representacao dos valores das variaveis inseridas na tabela 
        """ 
        verifica = self.buscarUsuario(usuario.codigo_usuario)
        if verifica == None:
            self.cursor.execute('INSERT INTO usuario(codigo_usuario, nome, cpf, telefone, endereco, bairro, cidade, cep, email, senha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (usuario.codigo_usuario, usuario.nome, usuario.cpf, usuario.telefone, usuario.endereco, usuario.bairro, usuario.cidade, usuario.cep, usuario.email, usuario.senha))
            self.conexao.commit()
            return True
        else:
            return False

        
    def buscarUsuario(self, codigo_usuario):
        """
        realiza a busca de um usuario pelo codigo do usuario informado.

        Parameters
        ----------
        codigo_usuario {string}:
            codigo de identificao do usuario em formato de string, que podera conter numero e/ou caracteres especiais ao se cadastrar
        return {boolean}: 
            referente ao retorno com o resultado do tipo None ou o proprio resultado das condicoes das funcoes
        usuario:
            referece um elemento intanciado da classe Usuario, que recebe uma lista. 
        """
        self.cursor.execute("SELECT * FROM usuario WHERE codigo_usuario = %s", (codigo_usuario,)) #executa a selecao do codigo do usuario na tabela usuario
        selecionar = self.cursor.fetchone() #recupera a próxima linha de um conjunto de resultados de consulta e retorna uma única sequência ou None, se não houver mais linhas disponíveis.
        if (selecionar == None):
            return None
        else:
            usuario = Usuario(selecionar[0],selecionar[1],selecionar[2],selecionar[3],selecionar[4],selecionar[5],selecionar[6],selecionar[7],selecionar[8],selecionar[9],selecionar[10])
            return usuario
    
    
    


    def cadastrarLivros(self, livro):
        """
        verifica se o codigo do livro informado corresponde aos dos livros ja cadastrados no sistema, caso nao, realiza o cadastro de um novo livro

        Parameters
        ----------
        codigo_livro {string}:
            codigo do livro em formato de string, que podera conter numero e/ou caracteres especiais
        return {boolean}: 
            referente ao retorno com o resultado em formato Boleano (verdadeiro ou falso) das condicoes das funcoes 
        """
        verifica = self.buscarLivros(livro.codigo_livro)
        if verifica == None:
            self.cursor.execute('INSERT INTO livro(codigo_livro, nome_autor, codigo_autor, titulo, editora, isbn, assunto, edicao, volume, Numero_pag, anoPublicacao, quantidade_exemplares) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d)', (livro.codigo_livro, livro.nome_autor, livro.codigo_autor, livro.titulo, livro.editora, livro.isbn, livro.assunto, livro.edicao, livro.volume, livro.Numero_pag, livro.anoPublicacao, livro.quantidade_exemplares))
            self.conexao.commit()
            return True
        else:
            return False

    def buscarLivros(self, codigo_livro):
        """
        realiza a busca de um livro pelo seu codigo.

        Parameters
        ----------
        codigo_livro {string}:
            codigo do livro em formato de string, que podera conter numero e/ou caracteres especiais.
        return {boolean}: 
            referente ao retorno com o resultado do tipo None ou o proprio resultado das condicoes das funcoes
        livro:
            referece um elemento intanciado da classe Livro, que recebe uma lista. 
        """
        self.cursor.execute("SELECT * FROM livro WHERE codigo_livro = %s", (codigo_livro,))
        selecionar = self.cursor.fetchone()
        if (selecionar == None):  # verifica se existe livro cadastrado
            return None
        else:
            livro = Livro(selecionar[0],selecionar[1],selecionar[2],selecionar[3],selecionar[4],selecionar[5],selecionar[6],selecionar[7],selecionar[8],selecionar[9], selecionar[10], selecionar[11])
            return livro

    def cadastrarExemplares(self, exemplar):
        """
        verifica se o codigo do exemplar informado corresponde aos dos exemplares ja cadastrados no sistema, caso nao, realiza o cadastro de um novo exemplar

        Parameters
        ----------
        codigo_exemplar {string}:
            codigo do exemplar de um livro em formato de string, que podera conter numero e/ou caracteres especiais
        return {boolean}: 
            referente ao retorno com o resultado em formato Boleano (verdadeiro ou falso) das condicoes das funcoes 
        """
        verifica = self.buscarExemplares(exemplar.codigo_exemplar)
        if verifica == None:
            self.cursor.execute('INSERT INTO exemplar(codigo_exemplar, codigo_livro, dias_emprestimo) VALUES(%s, %s, %s)', (exemplar.codigo_exemplar, exemplar.codigo_livro, exemplar.dias_emprestimo))
            self.conexao.commit()
            return True
        else:
            return False

    def buscarExemplares(self, codigo_exemplar):
        """
        realiza a busca de um exemplar de livro pelo seu codigo.

        Parameters
        ----------
        codigo_exemplar {string}:
            codigo do exemplar de um livro em formato de string, que podera conter numero e/ou caracteres especiais.
        return {boolean}: 
            referente ao retorno com o resultado do tipo None ou o proprio resultado das condicoes das funcoes
        exemplar:
            referece um elemento intanciado da classe Exemplar, que recebe uma lista. 
        """ 
        self.cursor.execute("SELECT * FROM exemplar WHERE codigo_exemplar = %s", (codigo_exemplar,))
        selecionar = self.cursor.fetchone()
        if (selecionar == None):  
            return None  
        else:
            exemplar = Exemplar(selecionar[0],selecionar[1],selecionar[2])
            return exemplar

    def realizarEmprestimo(self, emprestimo): #precisa ser ajustada, quando realizar um emprestimo o exemplar deve ser removido
        """
        verifica se o codigo do exemplar informado corresponde aos dos exemplares com registro de emprestimo  no sistema, caso nao, realiza o emprestimo de um exemplar de livro

        Parameters
        ----------
        codigo_exemplar {string}:
            codigo do exemplar de um livro em formato de string, que podera conter numero e/ou caracteres especiais
        return {boolean}: 
            referente ao retorno com o resultado em formato Boleano (verdadeiro ou falso) das condicoes das funcoes 
        """
        verifica = self.buscarEmprestimo(emprestimo.codigo_exemplar)
        if verifica == None:
            self.cursor.execute('INSERT INTO emprestimo(codigo_livro, codigo_exemplar, data_emprestimo, data_para_devolver) VALUES(%s, %s, %s, %s)', (emprestimo.codigo_livro, emprestimo.codigo_exemplar, emprestimo.data_emprestimo, emprestimo.data_para_devolver))
            #self.cursor.execute('DELETE FROM exemplar WHERE codigo_exemplar = %s', (exemplar.codigo_exemplar,))
            self.conexao.commit()
            return True
        else:
            return False

    def buscarEmprestimo(self, codigo_exemplar): 
        """
        realiza a busca de um emprestimo realizado pelo codigo do exemplar de livro.

        Parameters
        ----------
        codigo_exemplar {string}:
            codigo do exemplar de um livro em formato de string, que podera conter numero e/ou caracteres especiais.
        return {boolean}: 
            referente ao retorno com o resultado do tipo None ou o proprio resultado das condicoes das funcoes
        emprestimo:
            referece um elemento intanciado da classe Emprestimo, que recebe uma lista. 
        """
        self.cursor.execute("SELECT * FROM emprestimo WHERE codigo_exemplar = %s", (codigo_exemplar,))
        selecionar = self.cursor.fetchone()
        if (selecionar == None):
            return None
        else:
            emprestimo = Emprestimo(selecionar[0],selecionar[1],selecionar[2],selecionar[3], selecionar[4])
            return emprestimo

    def realizarDevolucao(self, devolucao): #precisa ser ajustada, quando realizar uma devolucao, este exemplar deve ser inserido novamente
        """
        verifica se o codigo do exemplar e a data da devolucao informado corresponde aos dos exemplares com registro de devolucoes no sistema, caso nao, realiza a devolucao do exemplar de um livro

        Parameters
        ----------
        codigo_exemplar {string}:
            codigo do exemplar de um livro em formato de string, que podera conter numeros e/ou caracteres especiais
        data_devolucao {string}:
            data da devolucao de um livro em formato de string, que podera conter numeros e/ou caracteres especiais
        return {boolean}: 
            referente ao retorno com o resultado em formato Boleano (verdadeiro ou falso) das condicoes das funcoes 
        """
        verifica = self.buscarDevolucoes(devolucao.codigo_exemplar, devolucao.data_devolucao)
        if verifica == None:
            self.cursor.execute('INSERT INTO devolucao(codigo_usuario, codigo_livro, codigo_exemplar, data_emprestimo, data_devolucao) VALUES(%s, %s, %s, %s, %s)', (devolucao.codigo_usuario, devolucao.codigo_livro, devolucao.codigo_exemplar, devolucao.data_emprestimo, devolucao.data_devolucao))
            self.conexao.commit()
            return True
        else:
            False

    def buscarDevolucoes(self, codigo_exemplar, data_devolucao):
        """
        realiza a busca da devolucao de um exemplar de livro por o codigo do exemplar do livro e a data da devolucao.

        Parameters
        ----------
        codigo_exemplar {string}:
            codigo do exemplar de um livro em formato de string, que podera conter numeros e/ou caracteres especiais.
        data_devolucao {string}:
            data da devolucao de um livro em formato de string, que podera conter numeros e/ou caracteres especiais
        return {boolean}: 
            referente ao retorno com o resultado do tipo None ou o proprio resultado das condicoes das funcoes
        emprestimo:
            referece um elemento intanciado da classe Emprestimo, que recebe uma lista. 
        """
        self.cursor.execute("SELECT * FROM devolucao WHERE codigo_exemplar = %s AND data_devolucao = %s", (codigo_exemplar, data_devolucao,))
        selecionar = self.cursor.fetchone()
        if (selecionar == None):
            return None
        else:
            devolucao = Devolucao(selecionar[0],selecionar[1],selecionar[2],selecionar[3],selecionar[4])
            return devolucao
        
    