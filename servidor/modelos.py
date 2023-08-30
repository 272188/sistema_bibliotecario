TABELAS = {
	'usuario': (
		"CREATE TABLE IF NOT EXISTS usuario ("
		"id_usuario INT AUTO_INCREMENT PRIMARY KEY,"
		"nome VARCHAR(100) NOT NULL,"
		"email VARCHAR(100) NOT NULL,"
		"senha VARCHAR(20) NOT NULL,"
		"cpf VARCHAR(14) NOT NULL,"
		"telefone VARCHAR(20) NOT NULL,"
		"endereco VARCHAR(60) NOT NULL,"
		"bairro VARCHAR(45) NOT NULL,"
		"cidade VARCHAR(45) NOT NULL,"
		"cep VARCHAR(20) NOT NULL,"
		"is_admin BOOLEAN NOT NULL DEFAULT FALSE"
		")"
	),
	'livro': (
		"CREATE TABLE IF NOT EXISTS livro ("
		"id_livro INT AUTO_INCREMENT PRIMARY KEY,"
		"nome_autor VARCHAR(100) NOT NULL,"
		"titulo VARCHAR(200) NOT NULL,"
		"editora VARCHAR(45) NOT NULL,"
		"isbn VARCHAR(20) NOT NULL,"
		"edicao VARCHAR(30) NOT NULL,"
		"volume VARCHAR(30) NOT NULL,"
		"numero_pag INT NOT NULL,"
		"ano_publicacao INT NOT NULL,"
		"ativo BOOLEAN NOT NULL DEFAULT TRUE"
		")"
	),
	'emprestimo': (
		"CREATE TABLE IF NOT EXISTS emprestimo ("
		"id_usuario INT NOT NULL,"
		"id_livro INT NOT NULL,"
		"data_emprestimo DATE NOT NULL,"
		"data_devolucao DATE NOT NULL,"
		"FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),"
		"FOREIGN KEY (id_livro) REFERENCES livro(id_livro)"
		")"
	),
}


class Usuario:
	"""
	Classe utilizada para representar as informacoes de um usuario do sistema

	...

	Attributes
	----------
	id_usuario : int
		codigo do usuario
	nome : str
		nome do usuario
	email : str
		email do usuario
	senha : str
		senha do usuario
	cpf : str
		cpf do usuario
	telefone : str
		telefone do usuario
	endereco : str
		endereco do usuario
	bairro : str
		bairro do usuario
	cidade : str
		cidade do usuario
	cep : str
		cep do usuario
	is_admin : bool
		tipo de usuario

	Methods
	-------
	__str__(self)
		Retorna uma string com os dados do usuario
	"""
	def __init__(self, id_usuario, nome, email, senha, cpf, telefone, endereco, bairro, cidade, cep, is_admin):
		"""
		Parameters
		----------
		id_usuario : int
			codigo do usuario
		nome : str
			nome do usuario
		email : str
			email do usuario
		senha : str
			senha do usuario
		cpf : str
			cpf do usuario
		telefone : str
			telefone do usuario
		endereco : str
			endereco do usuario
		bairro : str
			bairro do usuario
		cidade : str
			cidade do usuario
		cep : str
			cep do usuario
		is_admin : bool
			tipo de usuario
		"""
		self._id_usuario = id_usuario
		self._nome = nome
		self._email = email
		self._senha = senha
		self._cpf = cpf
		self._telefone = telefone
		self._endereco = endereco
		self._bairro = bairro
		self._cidade = cidade
		self._cep = cep
		self._is_admin = is_admin

	def __str__(self):
		return f'{self._id_usuario},{self._nome},{self._email},{self._senha},{self._cpf},{self._telefone},{self._endereco},{self._bairro},{self._cidade},{self._cep},{self._is_admin}'
	
	@property
	def id_usuario(self):
		return self._id_usuario
	
	@property
	def nome(self):
		return self._nome

	@property
	def email(self):
		return self._email
	
	@property
	def senha(self):
		return self._senha
	
	@property
	def cpf(self):
		return self._cpf
	
	@property
	def telefone(self):
		return self._telefone

	@property
	def endereco(self):
		return self._endereco

	@property
	def bairro(self):
		return self._bairro

	@property
	def cidade(self):
		return self._cidade

	@property
	def cep(self):
		return self._cep
	
	@property
	def is_admin(self):
		return self._is_admin


class Livro:
	"""
	Classe utilizada para representar um livro

	...

	Attributes
	----------
	id_livro : int
		codigo do livro
	nome_autor : str
		nome do autor
	titulo : str
		titulo do livro
	editora : str
		editora que publicou o livro
	isbn : str
		isbn de publicacao do livro
	edicao : str
		edicao do livro
	volume : int
		volume do livro
	numero_pag : int
		numero total de paginas do livro
	ano_publicacao : date
		ano de publicacao do livro

	Methods
	-------
	__str__(self)
		Retorna uma string com os dados do livro
	"""
	def __init__(self, id_livro, nome_autor, titulo, editora, isbn, edicao, volume, numero_pag, ano_publicacao, ativo):
		"""
		Parameters
        ----------
        id_livro : int, opcional
        	codigo do livro
        nome_autor : str, opcional
        	nome do autor
		titulo : str, opcional
			titulo do livro
		editora : str, opcional
			editora que piblicou o livro
		isbn : str, opcional
			isbn de publicacao do livro
		edicao : str, opcional
			edicao do livro
		volume : int, opcional
			volume do livro
		numero_pag : int, opcional
			numero total de paginas do livro
		ano_publicacao : date, opcional
			ano de publicacao do livro
		"""
		self._id_livro = id_livro
		self._nome_autor = nome_autor
		self._titulo = titulo
		self._editora = editora
		self._isbn = isbn
		self._edicao = edicao
		self._volume = volume
		self._numero_pag = numero_pag
		self._ano_publicacao = ano_publicacao
		self._ativo = ativo

	def __str__(self) -> str:
		return f'{self._id_livro},{self._nome_autor},{self._titulo},{self._editora},{self._isbn},{self._edicao},{self._volume},{self._numero_pag},{self._ano_publicacao},{self._ativo}'

	@property
	def id_livro(self):
		return self._id_livro
	
	@property
	def nome_autor(self):
		return self._nome_autor

	@property
	def titulo(self):
		return self._titulo

	@property
	def editora(self):
		return self._editora
	
	@property
	def isbn(self):
		return self._isbn
	
	@property
	def edicao(self):
		return self._edicao

	@property
	def volume(self):
		return self._volume

	@property
	def numero_pag(self):
		return self._numero_pag

	@property
	def ano_publicacao(self):
		return self._ano_publicacao
	
	@property
	def ativo(self):
		return self._ativo


class Emprestimo:
	"""
	Classe utilizada para representar um emprestimo

	...

	Attributes
	----------
	id_usuario : int
		codigo do usuario
	id_livro : int
		codigo do livro
	data_emprestimo : date
		data de emprestimo do livro
	data_devolucao : date

	Methods
	-------
	__str__(self)
		Retorna uma string com os dados do emprestimo
	"""
	def __init__(self, id_usuario, id_livro, data_emprestimo, data_devolucao):
		"""
		Parameters
		----------
		id_usuario : int
			codigo do usuario
		id_livro : int
			codigo do livro
		data_emprestimo : date
			data de emprestimo do livro
		data_devolucao : date
			data de devolucao do livro
		"""
		self._id_usuario = id_usuario
		self._id_livro = id_livro
		self._data_emprestimo = data_emprestimo
		self._data_devolucao = data_devolucao

	def __str__(self) -> str:
		return f'{self._id_usuario},{self._id_livro},{self._data_emprestimo},{self._data_devolucao}'
			
	@property
	def id_usuario(self):
		return self._id_usuario

	@property
	def id_livro(self):
		return self._id_livro

	@property
	def data_emprestimo(self):
		return self._data_emprestimo

	@property
	def data_devolucao(self):
		return self._data_devolucao
