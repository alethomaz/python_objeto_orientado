from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, endereco: int, cpf: int, nome: str):
        super().__init__(cpf, nome)
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        if isinstance(endereco, int):
            self.__endereco = endereco

    