from funcionario import Funcionario


class Caixa(Funcionario):

    def __init__(self, cpf: int, salario_base: float, adicional: float):
        super().__init__(cpf, salario_base)
        if isinstance(adicional, float):
            self.__adicional = adicional

    @property
    def adicional(self):
        return self.__adicional
    
    @adicional.setter
    def adicional(self, adicional: float):
        if isinstance(adicional, float):
            self.__adicional = adicional 

    def salario_total(self):
        return self.salario_base + self.__adicional

    