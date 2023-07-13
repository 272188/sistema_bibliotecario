from autor import Autor
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

	

	

	

	

	
	