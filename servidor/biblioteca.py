from modelos import Usuario, Livro, Emprestimo, TABELAS
import mysql.connector
import datetime


usuario = 'root'
senha = '1234'


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
    buscarUsuario(self, email)
        busca um usuario no banco de dados
    verificarLogin(self, email, senha)
        verifica se o login do usuario esta correto
    cadastrarUsuario(self, nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin=False)
        cadastra um usuario no banco de dados
    """
    def __init__(self):
        self.usuario = None
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = usuario,
            password= senha,
            auth_plugin='mysql_native_password',
        )
        self.cursor = self.conexao.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS bd_biblioteca")
        self.cursor.execute("USE bd_biblioteca")
        for tabela in TABELAS:
            self.cursor.execute(TABELAS[tabela])
        self.conexao.commit()

    def buscarUsuario(self, email):
        usuario = None
        self.cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
        selecionar = self.cursor.fetchone()
        if selecionar:
            usuario = Usuario(*selecionar)
        return usuario

    def verificarLogin(self, email, senha):
        usuario = self.buscarUsuario(email)
        if usuario and usuario.senha != senha:
            usuario = None
        self.usuario = usuario
        return usuario
    
    def fazerLogout(self):
        self.usuario = None

    def cadastrarUsuario(self, nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin=False):
        usuario = None
        buscar = self.buscarUsuario(email)
        if buscar == None:
            self.cursor.execute('INSERT INTO usuario(nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin))
            self.conexao.commit()
            usuario = self.buscarUsuario(email)
        return usuario
    
    def buscarLivro(self, id_livro):
        livro = None
        self.cursor.execute("SELECT * FROM livro WHERE id_livro = %s", (id_livro,))
        selecionar = self.cursor.fetchone()
        if selecionar:
            livro = Livro(*selecionar)
        return livro

    def cadastrarLivros(self, nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, qntd_exemplar):
        for i in range(qntd_exemplar):
            self.cursor.execute('INSERT INTO livro(nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, ativo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, 1 if i else 0))
        self.conexao.commit()

    def listarLivros(self, pesquisa):
        lista_livros = []
        self.cursor.execute("SELECT * FROM livro WHERE nome_autor = %s OR titulo = %s OR editora = %s OR isbn = %s", (pesquisa, pesquisa, pesquisa, pesquisa))
        selecionar = self.cursor.fetchall()
        for registro in selecionar:
            livro = Livro(*registro)
            lista_livros.append(livro)
        return lista_livros

    def buscarEmprestimo(self, id_livro):
        emprestimo = None
        self.cursor.execute("SELECT * FROM emprestimo WHERE id_usuario = %s AND id_livro = %s", (self.usuario.id_usuario, id_livro))
        selecionar = self.cursor.fetchone()
        if selecionar:
            emprestimo = Emprestimo(*selecionar)
        return emprestimo

    def realizarEmprestimo(self, id_livro):
        emprestimo = self.buscarEmprestimo(id_livro)
        if emprestimo == None:
            self.cursor.execute('INSERT INTO emprestimo(id_usuario, id_livro, data_emprestimo, data_devolucao) VALUES(%s, %s, %s, %s)', (self.usuario.id_usuario, id_livro, datetime.date.today(), datetime.date.today() + datetime.timedelta(days=7)))
            self.conexao.commit()
            emprestimo = self.buscarEmprestimo(id_livro)
        return emprestimo
    
    def listarEmprestimos(self):
        lista_emprestimos = []
        self.cursor.execute("SELECT * FROM emprestimo WHERE id_usuario = %s", (self.usuario.id_usuario,))
        selecionar = self.cursor.fetchall()
        for registro in selecionar:
            emprestimo = Emprestimo(*registro)
            lista_emprestimos.append(emprestimo)
        return lista_emprestimos


if __name__ == '__main__':
    bib = Biblioteca()
    bib.verificarLogin('joao@gmail.com', '1234')
    for emp in bib.listarEmprestimos():
        print(f'{str(bib.buscarLivro(emp.id_livro))[:-2]},{emp.data_emprestimo},{emp.data_devolucao}')