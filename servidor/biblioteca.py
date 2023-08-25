from modelos import Usuario, Livro, Emprestimo, TABELAS
import mysql.connector


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

    def cadastrarUsuario(self, nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin=False):
        usuario = None
        buscar = self.buscarUsuario(email)
        if buscar == None:
            self.cursor.execute('INSERT INTO usuario(nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin))
            self.conexao.commit()
            usuario = self.buscarUsuario(email)
        return usuario

    def buscarLivros(self, pesquisa):
        lista_livros = []
        self.cursor.execute("SELECT * FROM livro WHERE nome_autor = %s OR titulo = %s OR editora = %s OR isbn = %s", (pesquisa, pesquisa, pesquisa, pesquisa))
        selecionar = self.cursor.fetchall()
        for registro in selecionar:
            livro = Livro(*registro)
            lista_livros.append(livro)
        return lista_livros

    def cadastrarLivros(self, nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, qntd_exemplar):
        for i in range(qntd_exemplar):
            self.cursor.execute('INSERT INTO livro(nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, ativo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, 1))
        self.conexao.commit()

    def realizarEmprestimo(self, emprestimo):
        verifica = self.buscarEmprestimo(emprestimo.codigo_exemplar)
        if verifica == None:
            self.cursor.execute('INSERT INTO emprestimo(id_usuario, codigo_livro, codigo_exemplar, data_emprestimo, data_para_devolver) VALUES(%s, %s, %s, %s, %s)', (emprestimo.id_usuario, emprestimo.codigo_livro, emprestimo.codigo_exemplar, emprestimo.data_emprestimo, emprestimo.data_para_devolver))
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


if __name__ == '__main__':
    bib = Biblioteca()
    bib.cadastrarLivros(
        nome_autor='Carlos',
        titulo='Poemas',
        editora='Editora',
        isbn='123456789',
        edicao='3',
        volume='1',
        numero_pag='25',
        ano_publicacao='2003',
        qntd_exemplar=5
    )
    # user = bib.cadastrarUsuario(
    #     nome='Sheila',
    #     email='sheila.psb@gmail.com',
    #     senha='1234',
    #     cpf='12345678910',
    #     telefone='(83) 99999-9999',
    #     endereco='Rua X',
    #     bairro='Centro',
    #     cidade='João Pessoa',
    #     cep='58000-000',
    #     is_admin=True
    # )
    # print(user)
    # bib.verificarLogin(
    #     email='sheila.psb@gmail.com',
    #     senha='1234',
    # )
    # print(bib.usuario)