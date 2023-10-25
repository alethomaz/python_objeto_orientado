

class Cliente():
    def __init__(self, cpf: str, nome: str, endereco: str, telefone: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def cpf(self):
        return self.__cpf   

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def endereco(self):
        return self.__endereco   

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone   

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone
        
    @property
    def nome(self):
        return self.__nome   

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
        