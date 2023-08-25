class Usuario:
	"""

	Classe utilizada para representar as informacoes de um usuario do sistema

	
	"""
	__slots__ = ['__codigo_usuario', '__nome', '__cpf', '__telefone', '__endereco', '__bairro', '__cidade', '__cep', '__email', '__senha', '__tipo']

	def __init__(self, codigo_usuario, nome, cpf, telefone, endereco, bairro, cidade, cep, email, senha, tipo):
		self.__codigo_usuario = codigo_usuario
		self.__nome = nome
		self.__cpf = cpf
		self.__telefone = telefone
		self.__endereco = endereco
		self.__bairro = bairro
		self.__cidade = cidade
		self.__cep = cep
		self.__email = email
		self.__senha = senha
		self.__tipo = tipo

	def __str__(self):
		return f'{self.__codigo_usuario},{self.__nome},{self.__cpf},{self.__telefone},{self.__endereco},{self.__bairro},{self.__cidade},{self.__cep},{self.__email},{self.__senha},{self.__tipo}'
	
	@property
	def codigo_usuario(self):
		return self.__codigo_usuario
	
	@codigo_usuario.setter
	def codigo_usuario(self, codigo_usuario):
		self.__codigo_usuario = codigo_usuario
	
	@property
	def nome(self):
		return self.__nome
	
	@nome.setter
	def nome(self, nome):
		self.__nome = nome
	
	@property
	def cpf(self):
		return self.__cpf
	@cpf.setter
	def cpf(self, cpf):
		self.__cpf = cpf
	
	@property
	def telefone(self):
		return self.__telefone
	@telefone.setter
	def telefone(self, telefone):
		self.__telefone = telefone

	@property
	def endereco(self):
		return self.__endereco
	@endereco.setter
	def endereco(self, end):
		self.__endereco = end

	@property
	def bairro(self):
		return self.__bairro
	@bairro.setter
	def bairro(self, bairro):
		self.__bairro = bairro

	@property
	def cidade(self):
		return self.__cidade
	@cidade.setter
	def cidade(self, cidade):
		self.__cidade = cidade

	@property
	def cep(self):
		return self.__cep
	@cep.setter
	def cep(self, cep):
		self.__cep = cep

	@property
	def email(self):
		return self.__email
	@email.setter
	def email(self, email):
		self.__email = email
	
	@property
	def senha(self):
		return self.__senha
	@senha.setter
	def senha(self, senha):
		self.__senha = senha
	
	@property
	def tipo(self):
		return self.__tipo
	@tipo.setter
	def tipo(self, tipo):
		self.__tipo = tipo


class Pessoa:
	
	'''
       classe Pessoa recebe como parametro um nome e sobrenome do autor
    '''
    
	def __init__(self, nome_autor, sobrenome):
		self.__nome_autor = nome_autor
		self.__sobrenome = sobrenome

	@property
	def nome_autor(self):
		return self.__nome_autor
	@nome_autor.setter
	def nome_autor(self, nome_autor):
		self.__nome_autor = nome_autor

	@property
	def sobrenome(self):
		return self.__sobrenome
	@sobrenome.setter
	def sobrenome(self, sobrenome):
		self.__sobrenome = sobrenome


class Autor(Pessoa):
    """
    A classe utilizada para representar um autor

    
    """

    def __init__(self, codigo_autor, nome_autor):
        """

        Parametros
        ----------
        codigo_autor : int, opcional
            codigo do autor
        nome_autor : str, opcional
            nome do autor
        """
        super(Pessoa, self).__init__()
        self.__codigo_autor = codigo_autor
        self.__nome_autor = nome_autor

    @property
    def codigo_autor(self):
        return self.__codigo_autor
    @codigo_autor.setter
    def codigo_autor(self, codigo_autor):
        self.__codigo_autor = codigo_autor

    @property
    def nome_autor(self):
        return self.__nome_autor
    @nome_autor.setter
    def nome_autor(self, nome_autor):
        self.__nome_autor = nome_autor


class Livro:
	"""

	Classe utilizada para representar um livro


	"""
	def __init__(self, codigo_livro, nome_autor, codigo_autor, titulo, editora, isbn, assunto, edicao, volume, Numero_pag, anoPublicacao):
		"""
		Parametros
        ----------
        codigo_livro : int, opcional
        	codigo do livro
        nome_autor : str, opcional
        	nome do autor
		codigo_autor : int, opcional
			codigo do autor
		titulo : str, opcional
			titulo do livro
		editora : str, opcional
			editora que piblicou o livro
		isbn : str, opcional
			isbn de publicacao do livro
		assunto : str, opcional
			assunto referente a abordagem do livro
		edicao : str, opcional
			edicao do livro
		volume : int, opcional
			volume do livro
		Numero_pag : int, opcional
			numero total de paginas do livro
		anoPublicacao : date, opcional
			ano de publicacao do livro
		"""
		
		self.__codigo_livro = codigo_livro
		self.__nome_autor = nome_autor
		self.__codigo_autor = codigo_autor
		self.__titulo = titulo
		self.__editora = editora
		self.__isbn = isbn
		self.__assunto = assunto
		self.__edicao = edicao
		self.__volume = volume
		self.__Numero_pag = Numero_pag
		self.__anoPublicacao = anoPublicacao
		
		
	@property
	def codigo_livro(self):
		return self.__codigo_livro
	@codigo_livro.setter
	def codigo_livro(self, codigo_livro):
		self.__codigo_livro = codigo_livro
	
	@property
	def nome_autor(self):
		return self.__nome_autor
	@nome_autor.setter
	def nome_autor(self, nome_autor):
		self.__nome_autor = nome_autor
	
	@property
	def codigo_autor(self):
		return self.__codigo_autor
	@codigo_autor.setter
	def codigo_autor(self, codigo_autor):
		self.__codigo_autor = codigo_autor

	@property
	def titulo(self):
		return self.__titulo
	@titulo.setter
	def titulo(self, titulo):
		self.__titulo = titulo

	@property
	def editora(self):
		return self.__editora
	@editora.setter
	def editora(self, editora):
		self.__editora = editora
	
	@property
	def isbn(self):
		return self.__isbn
	@isbn.setter
	def isbn(self, isbn):
		self.__isbn = isbn
	
	@property
	def assunto(self):
		return self.__assunto
	@assunto.setter
	def assunto(self, assunto):
		self.__assunto = assunto
	
	@property
	def edicao(self):
		return self.__edicao
	@edicao.setter
	def edicao(self, edicao):
		self.__edicao = edicao

	@property
	def volume(self):
		return self.__volume
	@volume.setter
	def volume(self, volume):
		self.__volume = volume

	@property
	def Numero_pag(self):
		return self.__Numero_pag
	@Numero_pag.setter
	def Numero_pag(self, Numero_pag):
		self.__Numero_pag = Numero_pag

	@property
	def anoPublicacao(self):
		return self.__anoPublicacao
	@anoPublicacao.setter
	def anoPublicacao(self, anoPublicacao):
		self.__anoPublicacao = anoPublicacao
		

class Exemplar:
#codigo livro, codigo_exemplar, ativo, motivo_baixa, dias_emprestimo
	def __init__(self, codigo_exemplar, codigo_livro, dias_emprestimo):
		self.__codigo_exemplar = codigo_exemplar
		self.__codigo_livro = codigo_livro
		self.__ativo = True
		self.__dias_emprestimo = dias_emprestimo

	@property
	def codigo_exemplar(self):
		return self.__codigo_exemplar
	@codigo_exemplar.setter
	def codigo_exemplar(self, codigo_exemplar):
		self.__codigo_exemplar = codigo_exemplar
	
	@property
	def codigo_livro(self):
		return self.__codigo_livro
	@codigo_livro.setter
	def codigo_livro(self, codigo_livro):
		self.__codigo_livro = codigo_livro

	@property
	def ativo(self):
		return self.__ativo
	@ativo.setter
	def ativo(self, ativo):
		self.__ativo = ativo

	'''@property
	def motivo_baixa(self):
		return self.__motivo_baixa
	@motivo_baixa.setter
	def motivo_baixa(self, motivo):
		self.__motivo_baixa = motivo'''
	
	@property
	def dias_emprestimo(self):
		return self.__dias_emprestimo
	@dias_emprestimo.setter
	def dias_emprestimo(self, dias_emprestimo):
		self.__dias_emprestimo = dias_emprestimo

	'''def darBaixa(self, motivo):
		self.__ativo = False
		self.__motivo_baixa = motivo'''


class Emprestimo:
	def __init__(self, codigo_usuario, codigo_livro, codigo_exemplar, data_emprestimo, data_para_devolver):
			self.__codigo_usuario = codigo_usuario
			self.__codigo_livro = codigo_livro
			self.__codigo_exemplar = codigo_exemplar
			self.__data_emprestimo = data_emprestimo
			self.__data_para_devolver = data_para_devolver
			

	@property
	def codigo_usuario(self):
		return self.__codigo_usuario
	@codigo_usuario.setter
	def codigo_usuario(self, codigo_usuario):
		self.__codigo_usuario = codigo_usuario

	@property
	def codigo_livro(self):
		return self.__codigo_livro
	@codigo_livro.setter
	def codigo_livro(self, codigo_livro):
		self.__codigo_livro = codigo_livro
	
	@property
	def codigo_exemplar(self):
		return self.__codigo_exemplar
	@codigo_exemplar.setter
	def codigo_exemplar(self, codigo_exemplar):
		self.__codigo_exemplar = codigo_exemplar

	@property
	def data_emprestimo(self):
		return self.__data_emprestimo
	@data_emprestimo.setter
	def data_emprestimo(self, data_emprestimo):
		self.__data_emprestimo = data_emprestimo

	@property
	def data_para_devolver(self):
		return self.__data_para_devolver
	@data_para_devolver.setter
	def data_para_devolver(self, data_para_devolver):
		self.__data_para_devolver = data_para_devolver


class Devolucao:
	def __init__(self, codigo_usuario, codigo_livro, codigo_exemplar, data_emprestimo, data_devolucao):
			self.__codigo_usuario = codigo_usuario
			self.__codigo_exemplar = codigo_exemplar
			self.__codigo_livro = codigo_livro
			self.__data_emprestimo = data_emprestimo
			self.__data_devolucao = data_devolucao
			#self.__devolvido = True
			#self.__data_devolucao = None

	@property
	def codigo_usuario(self):
		return self.__codigo_usuario
	@codigo_usuario.setter
	def codigo_usuario(self, codigo_usuario):
		self.__codigo_usuario = codigo_usuario

	@property
	def codigo_livro(self):
		return self.__codigo_livro
	@codigo_livro.setter
	def codigo_livro(self, codigo_livro):
		self.__codigo_livro = codigo_livro

	@property
	def codigo_exemplar(self):
		return self.__codigo_exemplar
	@codigo_exemplar.setter
	def codigo_exemplar(self, codigo_exemplar):
		self.__codigo_exemplar = codigo_exemplar
	
	@property
	def data_emprestimo(self):
		return self.__data_emprestimo
	@data_emprestimo.setter
	def data_emprestimo(self, data_emprestimo):
		self.__data_emprestimo = data_emprestimo

	'''@property
	def data_para_devolver(self):
		return self.__data_para_devolver
	@data_para_devolver.setter
	def data_para_devolver(self, data_para_devolver):
		self.__data_para_devolver = data_para_devolver

	@property
	def devolvido(self):
		return self.__devolvido
	@devolvido.setter
	def devolvido(self, devolvido):
		self.__devolvido = devolvido'''

	@property
	def data_devolucao(self):
		return self.__data_devolucao
	@data_devolucao.setter
	def data_devolucao(self, data_devolucao):
		self.__data_devolucao = data_devolucao