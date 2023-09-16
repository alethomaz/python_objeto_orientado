from funcionario import Funcionario


class Vendedor(Funcionario):

    def __init__(self, cpf: int, salario_base: float, comissao: float, total_vendas: float):
        super().__init__(cpf, salario_base)
        if isinstance(comissao, float):
            self.__comissao = comissao
        if isinstance(total_vendas, float):
            self.__total_vendas = total_vendas

    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.setter
    def comissao(self, comissao: float):
        if isinstance(comissao, float):
            self.__comissao = comissao

    @property
    def total_vendas(self):
        return self.__total_vendas
    
    @total_vendas.setter
    def total_vendas(self, total_vendas: float):
        if isinstance(total_vendas, float):
            self.__total_vendas = total_vendas

    def salario_total(self):
        return self.salario_base + ((self.__comissao * self.__total_vendas ) / 100)
    