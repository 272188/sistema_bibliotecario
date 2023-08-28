#importação das classes
from modelos import Usuario, Livro, Emprestimo, TABELAS


from datetime import date

#importação do banco de dados
import mysql.connector

usuario = 'sheila'
senha = 'root'


class Biblioteca:
    """

	Classe que representa a biblioteca, responsável por realizar as operações no banco de dados.

    ...

    Attributes
    ----------
    usuario : Usuario
        usuario que esta utilizando o sistema
    conexao : mysql.connector.connect
        conexao com o banco de dados
    cursor : mysql.connector.cursor
        cursor para realizar as operacoes no banco de dados
 
    
     Methods
    -------
    verificarLogin(self, email, senha):
        verfifica se o email e a senha esta correto, usuario cadastrado no sistema
    cadastrarUsuario(self, nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin=False):
        cadastra um usuario no banco de dados.
    buscarUsuario(self, email):
        faz uma busca do usuario no bano de dados.
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
        self.usuario = None
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = usuario,
            password= senha,
            auth_plugin = 'mysql_native_password',
        
        )
        self.cursor = self.conexao.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS banco_bib") #funcao para executar a acao no mysql
        self.cursor.execute("USE banco_bib")
        for tabela in TABELAS:
            self.cursor.execute(TABELAS[tabela])
        self.conexao.commit() #Por padrão, não é efetuado commit automaticamente, deve-se commitar para salvar as alteracoes no banco.
        
        

    def verificarLogin(self, email, senha):
        """
        verifica se o email e senha informado corresponde aos dos usuarios ja cadastrados no sistema e assim, permitir logar no sistema.

        Parameters
        ----------
        email {string}:
            email do usuario informado ao se cadastrar no sistema
        senha {string} :
            hash da senha em formato de string para garatir a seguranca no acesso ao sistema
        return {boolean}: 
            Boleano referente ao resultado para retorno das condicoes das funcoes
        """

        usuario = self.buscarUsuario(email)
        if usuario and usuario.senha != senha:
            usuario = None
        self.usuario = usuario
        return usuario

    def cadastrarUsuario(self, nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin=False):
        """
        verifica se oemail do usuario informado corresponde aos dos usuarios ja cadastrados no sistema, caso nao, solicita-se realizar o cadastro de novo usuario no sistema

        Parameters
        ----------
        nome {string}:
            nome do usuario em formato de string.
        email {string}:
            email do usuario em formato de string.
        senha {string}:
            senha do usuario em formato de string, podera conter numeros e/ou caracteres especiais.
        cpf {string}:
            cpf do usuario em formato de string, podera conter caracteres especiais.
        telefone {string}:
            telefone do usuario em formato de string, podera conter caracteres especiais.
        endereco {string}:
            endereco de residencia em formato de string, podera ser o nome da rua/avenida/praca e o numero da residencia.
        bairro {string}:
            bairro de residencia em formato de string.
        cidade {string}:
            cidade de residencia em formato de string.
        cep {string}:
            cep de localizacao da residencia em formato de string.
        is_admin {boolean}:
            tipo de usuario para devido acesso as funcionalidades do sistema em formato de boolean.
        VALUES:
            refere-se formato de representacao dos valores das variaveis inseridas na tabela 
        """ 
        usuario = None
        buscar = self.buscarUsuario(email)
        if buscar == None:
            self.cursor.execute('INSERT INTO usuario(nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin))
            self.conexao.commit()
            usuario = self.buscarUsuario(email)
        return usuario

        
    def buscarUsuario(self, email):
        """
        realiza a busca de um usuario pelo codigo do usuario informado.

        Parameters
        ----------
        email {string}:
            email do usuario em formato de string, informado ao se cadastrar.
        return {boolean}: 
            referente ao retorno com o resultado do tipo None ou o proprio resultado das condicoes das funcoes
        usuario:
            referece um elemento intanciado da classe Usuario, que recebe None como parametro padrao 
        """
        usuario = None
        self.cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
        selecionar = self.cursor.fetchone()
        if selecionar:
            usuario = Usuario(*selecionar)
        return usuario
    
    
    def cadastrarLivros(self, nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, qntd_exemplar):
        """
        verifica se o codigo do livro informado corresponde aos dos livros ja cadastrados no sistema, caso nao, realiza o cadastro de um novo livro

        Parameters
        ----------
        nome_autor {string}:
            nome do autor do livro em formato de string.
        titulo {string}:
            titulo do livro em formato de string.
        editora {string}:
            nome da editora que publicou o livro em formato de string.
        isbn {string}:
            codigo de publicacao do livro em formato de string.
        edicao {string}:
            numero da edicao do livro em formato de string.
        volume {int}:
            numero do volume do livro em formato de numero inteiro.
        numero_pag {int}:
            quantidade total de paginas contidas no livro em formato de string.
        ano_publicacao {string}:
            ano em o livro foi publicado em formato de string.
        qntd_exemplar {int}:
            quantidade de exemplares que o livro possui em formato de numero inteiro.
        return {boolean}: 
            referente ao retorno com o resultado em formato Boleano (verdadeiro ou falso) das condicoes das funcoes 
        """
        for i in range(qntd_exemplar):
            self.cursor.execute('INSERT INTO livro(nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, ativo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, 1))
        self.conexao.commit()

    def buscarLivros(self, pesquisa):
        """
        realiza a busca de livros cadastrados no sistema pelo nome do autor/titulo do livro/nome da editora/codigo de publicação(isbn).

        Parameters
        ----------
        pesquisa:
            pesquisa livros cadastrados no banco de dados do sistema pelo nome do autor/titulo do livro/nome da editora/codigo de publicação(isbn).
        return {boolean}: 
            referente ao retorno com o resultado do tipo None ou o proprio resultado das condicoes das funcoes
        livro:
            referece um elemento intanciado da classe Livro, que recebe uma lista. 
        """
        lista_livros = []
        self.cursor.execute("SELECT * FROM livro WHERE nome_autor = %s OR titulo = %s OR editora = %s OR isbn = %s", (pesquisa, pesquisa, pesquisa, pesquisa))
        selecionar = self.cursor.fetchall()
        for registro in selecionar:
            livro = Livro(*registro)
            lista_livros.append(livro)
        return lista_livros

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
    '''
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
        
    '''