from abc import ABC, abstractclassmethod


class Pessoa(ABC):
    @abstractclassmethod
    def __init__(self, nome: str, cpf: int):
        self.__nome = nome
        self.__cpf = cpf

    
