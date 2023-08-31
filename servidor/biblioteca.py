from modelos import Usuario, Livro, Emprestimo, TABELAS
import mysql.connector
import datetime


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
    buscarUsuario(self, email)
        busca um usuario no banco de dados
    verificarLogin(self, email, senha)
        verifica se o login do usuario esta correto
    cadastrarUsuario(self, nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin=False)
        cadastra um usuario no banco de dados
    _emprestimos_usuario(self, id_usuario):
        Obtém uma lista de empréstimos associados a um usuário específico, ou seja, realiza uma consulta ao banco de dados para buscar todos os registros de empréstimos que estão associados ao ID de usuário fornecido.
    excluirUsuario(self, email):
        Exclui um usuário do sistema com base no email fornecido. Ele verifica se o usuário com o email fornecido existe. Se o usuário existe e não possui empréstimos ativos, o método prossegue para excluir o usuário do banco de dados.
    listarUsuarios(self):
        Lista todos os usuários cadastrados no sistema, exceto o usuário atualmente logado. Ele executa uma consulta SQL para selecionar todos os registros da tabela 'usuario'.
    buscarLivro(self, id_livro):
        Busca um livro no sistema com base no ID do livro fornecido.
    cadastrarLivros(self, nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, qntd_exemplar):
        Cadastra múltiplos exemplares do mesmo livro no sistema. Ele itera sobre um intervalo de acordo com a quantidade de exemplares a serem cadastrados.
    _emprestimos_livro(self, id_livro):
        Este método realiza uma consulta ao banco de dados para buscar todos os registros de empréstimos que estão associados ao ID do livro fornecido.
    def excluirLivro(self, id_livro):
        Este método tenta excluir um livro do sistema com base no ID fornecido.
    listarLivros(self, pesquisa):
        Lista os livros cadastrados no sistema que correspondem à pesquisa fornecida.
    buscarEmprestimo(self, id_livro):
        Busca um empréstimo no sistema com base no ID do livro e no ID do usuário atual.
    realizarEmprestimo(self, id_livro, data_emprestimo=datetime.date.today(), data_devolucao=datetime.date.today() + datetime.timedelta(days=7)):
        Verificar se um empréstimo já existe para o livro fornecido caso não, realiza um empréstimo de um livro para o usuário atual.
    realizarDevolucao(self, id_livro):
        Realiza a devolução de um livro previamente emprestado pelo usuário atual.
    listarEmprestimos(self):
        Lista os empréstimos realizados pelo usuário atual.
    fechar_bd(self):
        Fecha a conexão com o banco de dados.
     
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
    
    def _emprestimos_usuario(self, id_usuario):
        lista_emprestimos = []
        self.cursor.execute("SELECT * FROM emprestimo WHERE id_usuario = %s", (id_usuario,))
        selecionar = self.cursor.fetchall()
        for registro in selecionar:
            emprestimo = Emprestimo(*registro)
            lista_emprestimos.append(emprestimo)
        return lista_emprestimos
    
    def excluirUsuario(self, email):
        excluiu = False
        usuario = self.buscarUsuario(email)
        if usuario != None and not self._emprestimos_usuario(usuario.id_usuario):
            self.cursor.execute('DELETE FROM usuario WHERE email = %s', (email,))
            self.conexao.commit()
            excluiu = True
        return excluiu
    
    def listarUsuarios(self):
        lista_usuarios = []
        self.cursor.execute("SELECT * FROM usuario")
        selecionar = self.cursor.fetchall()
        for registro in selecionar:
            usuario = Usuario(*registro)
            if usuario.id_usuario != self.usuario.id_usuario:
                lista_usuarios.append(usuario)
        return lista_usuarios
    
    def buscarLivro(self, id_livro):
        livro = None
        self.cursor.execute("SELECT * FROM livro WHERE id_livro = %s", (id_livro,))
        selecionar = self.cursor.fetchone()
        if selecionar:
            livro = Livro(*selecionar)
        return livro

    def cadastrarLivros(self, nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, qntd_exemplar):
        for i in range(int(qntd_exemplar)):
            self.cursor.execute('INSERT INTO livro(nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, ativo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, 1 if i else 0))
        self.conexao.commit()

    def _emprestimos_livro(self, id_livro):
        lista_emprestimos = []
        self.cursor.execute("SELECT * FROM emprestimo WHERE id_livro = %s", (id_livro,))
        selecionar = self.cursor.fetchall()
        for registro in selecionar:
            emprestimo = Emprestimo(*registro)
            lista_emprestimos.append(emprestimo)
        return lista_emprestimos

    def excluirLivro(self, id_livro):
        excluiu = False
        livro = self.buscarLivro(id_livro)
        #Se o livro existe e não possui empréstimos ativos, o método prossegue para excluir o livro do banco de dados.
        if livro != None and self._emprestimos_livro(id_livro) == []:   
            self.cursor.execute('DELETE FROM livro WHERE id_livro = %s', (id_livro,))
            self.conexao.commit()
            excluiu = True
        return excluiu

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

    def realizarEmprestimo(self, id_livro, data_emprestimo=datetime.date.today(), data_devolucao=datetime.date.today() + datetime.timedelta(days=7)):
        emprestimo = self.buscarEmprestimo(id_livro)
        if emprestimo == None:
            livro = self.buscarLivro(id_livro)
            if livro and livro.ativo:
                self.cursor.execute('INSERT INTO emprestimo(id_usuario, id_livro, data_emprestimo, data_devolucao) VALUES(%s, %s, %s, %s)', (self.usuario.id_usuario, id_livro, data_emprestimo, data_devolucao))
                self.cursor.execute('UPDATE livro SET ativo = 0 WHERE id_livro = %s', (id_livro,))
                self.conexao.commit()
                emprestimo = self.buscarEmprestimo(id_livro)
        else:
            emprestimo = None
        return emprestimo
    
    def realizarDevolucao(self, id_livro):
        devolveu = False
        emprestimo = self.buscarEmprestimo(id_livro)
        if emprestimo != None:
            self.cursor.execute('DELETE FROM emprestimo WHERE id_usuario = %s AND id_livro = %s', (self.usuario.id_usuario, id_livro))
            self.cursor.execute('UPDATE livro SET ativo = 1 WHERE id_livro = %s', (id_livro,))
            self.conexao.commit()
            devolveu = True
        return devolveu
    
    def listarEmprestimos(self):
        lista_emprestimos = []
        self.cursor.execute("SELECT * FROM emprestimo WHERE id_usuario = %s", (self.usuario.id_usuario,))
        selecionar = self.cursor.fetchall()
        for registro in selecionar:
            emprestimo = Emprestimo(*registro)
            lista_emprestimos.append(emprestimo)
        return lista_emprestimos
    
    def fechar_bd(self):
        self.conexao.close()

'''
if __name__ == '__main__':
    bib = Biblioteca()
    bib.verificarLogin('romuere@gmail.com', '000')
    print (bib.realizarEmprestimo(4, data_emprestimo=datetime.date(2023, 8, 1), data_devolucao=datetime.date(2023, 8, 8)))
    bib.fechar_bd()

if __name__ == '__main__':
    bib = Biblioteca()
    bib.cadastrarUsuario(
        nome='Admin',
        email='admin@gmail.com',
        senha='1234',
        cpf='12345678910',
        telefone='(11) 11111-1111',
        endereco='Rua 1',
        bairro='Bairro 1',
        cidade='Cidade 1',
        cep='11111-111',
        is_admin=True
    )
    bib.fechar_bd()
'''