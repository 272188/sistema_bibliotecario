class Usuario:
	"""

	Classe utilizada para representar as informacoes de um usuario do sistema

	
	"""
	__slots__ = ['__codigo_usuario', '__nome', '__cpf', '__telefone', '__endereco', '__bairro', '__cidade', '__cep', '__email', '__senha', '__tipo']

	def __init__(self, codigo_usuario, nome, cpf, telefone, endereco, bairro, cidade, cep, email, senha, tipo):
		"""
		Parameters
		----------
		codigo_usuario : int, optional
			codigo do usuario
		nome : str, optional
			nome do usuario
		cpf : str, optional
			cpf do usuario
		telefone : str, optional
			telefone para contato do usuario
		endereco : str, optional
			endereco de residencia do usuario
		bairro : str, optional
			bairro de residencia do usuario
		cidade : str, optional
			cidade de residencia do usuario
		cep : str, optional
			cep da cidade de residencia do usuario
		email : str, optional
			email do usuario
		senha : str, optional
			senha de acesso do usuario
		tipo : str, optional
			tipo de usuario para acesso ao sistema
		"""
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

	
	