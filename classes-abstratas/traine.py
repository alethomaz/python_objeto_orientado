from funcionario import Funcionario


class Trainee(Funcionario):

    def __init__(self, cpf: int, salario_base: float):
        super().__init__(cpf, salario_base)

    def salario_total(self):
        return self.salario_base / 2