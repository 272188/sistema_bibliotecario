from pessoa import Pessoa


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
