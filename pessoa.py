class Pessoa:
	
	'''
       classe Pessoa recebe como parametro um nome e sobrenome do autor
    '''
    
	def __init__(self, nome_autor, sobrenome):
		"""
		Parameters
		----------
		nome_autor : str, optional
			nome do autor
		sobrenome : str, optional
			sobrenome do autor
		"""
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
