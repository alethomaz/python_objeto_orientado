

class ItemPedido():
    def __init__(self, codigo: int, descricao: str, preco: float):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @preco.setter
    def preco(self, preco: float):
        self.__preco = preco