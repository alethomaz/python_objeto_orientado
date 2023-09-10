from pessoa import Pessoa


class Vendedor(Pessoa):
    def __init__(self, comissao: int, cpf: int, nome: str):
        super().__init__(cpf, nome)
        if isinstance(comissao, int):
            self.__comissao = comissao
        print('Objeto vendedor instanciado')
        print(self, 'cadastrado')

    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.setter
    def comissao(self, comissao):
        if isinstance(comissao, int):
            self.__comissao

    def __repr__(self):
        return f'Vendedor {self.nome}'

            