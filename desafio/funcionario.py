from pessoa import Pessoa
from cargo import Cargo
from dependente import Dependente


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: int, cargo: Cargo):
        super().__init__(nome, cpf)
        self.__cargo = cargo
        self.__dependentes = []


    def add_dependente(self, nome: str, cpf: int):
        cpfs = [dependente.cpf for dependente in self.__dependentes]
        if cpf not in cpfs:
            dependente = Dependente(nome, cpf)
            self.__dependentes.append(dependente)
        

    def rem_dependente(self, nome: str, cpf: int):
        cpfs = [dependente.cpf for dependente in self.__dependentes]
        if cpf in cpfs:
            indice = cpfs.index(cpf)
            self.dependentes.remove(self.dependentes[indice])