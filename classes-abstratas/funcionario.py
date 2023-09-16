from abc import ABC, abstractmethod

# Subclasse Funcionário
class Funcionario(ABC):
    
    # Nãp se ṕde croar isntâncias a partir da classe Funcionário
    @abstractmethod
    def __init__(self, cpf: int, salario_base: float):
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(salario_base, float):
            self.__salario_base = salario_base

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: int): 
        self.__cpf = cpf

    @property
    def salario_base(self):
        return self.__salario_base
    
    @salario_base.setter
    def salario_base(self, salario_base: float):
        if isinstance(salario_base, float):
            self.__salario_base = salario_base

    
    @abstractmethod
    def salario_total(self) -> float:
        return self.__salario_total
    
    