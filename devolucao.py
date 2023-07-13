from usuario import Usuario
from autor import Autor
from livro import Livro
from exemplar import Exemplar
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