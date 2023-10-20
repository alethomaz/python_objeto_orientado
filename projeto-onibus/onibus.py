from abstractOnibus import AbstractOnibus


class Onibus(AbstractOnibus):

    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        self._capacidade = capacidade
        self._total_passageiros = total_passageiros
        self._ligado = ligado

    def ligar(self) -> str:
        if self.__ligado:
            raise Exception('Onibus já está ligado')
        else:
            self.__ligado = True
            return 'Onibus ligado'
        
    def desligar(self) -> str:
        if self.__ligado:
            self.__ligado == False
            return 'Onibus desligado'
        else:
            raise Exception('Onibus já está desligado')
        
    def entrar_onibus(self):
        pass
    