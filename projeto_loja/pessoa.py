

class Pessoa:

    def __init__(self, cpf: int, nome: str): 
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, int):
            self.__cpf = cpf


    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
            
             

        