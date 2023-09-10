

class Produto:

    def __init__(self, codigo, descricao, categoria):

        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria
        self.__quantidade = None
        self.__preco_unitario = None
        self.__cliente = None

    @property
    def codigo(self):
        return self.__codigo

    codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @


