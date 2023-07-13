from livro import Livro

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
	