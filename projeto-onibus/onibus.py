from abstractOnibus import AbstractOnibus


class Onibus(AbstractOnibus):

    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        self.__capacidade = capacidade
        self.__total_passageiros = total_passageiros
        self.__ligado = ligado

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    @property
    def total_passageiros(self) -> int:
        return self.__total_passageiros

    def ligar(self) -> str:
        if self.__ligado:
            raise Exception('Onibus já está ligado')
        else:
            self.__ligado = True
            return 'Onibus ligado'
        
    def embarca_pessoa(self) -> str:
        print('Um passageiro entrou no onibus')
        self.__total_passageiros += 1 

    def desembarca_pessoa(self) -> str:
        print('Passageiro saiu do onibus')
        self.__total_passageiros -= 1 

    def desligar(self) -> str:
        if self.__ligado:
            self.__ligado == False
            return 'Onibus desligado'
        else:
            raise Exception('Onibus já está desligado')
        
    def entrar_onibus(self):
        pass
    
    def ligado(self):
        pass