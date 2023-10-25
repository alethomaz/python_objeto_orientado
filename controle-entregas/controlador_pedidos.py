from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos:
    def __init__(self):
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    '''
    Busca pedido pelo numero.
    Se o pedido nao existir, deve retornar None
    Caso contrario, retorna o pedido.
    '''
    def busca_pedido_por_numero(self, numero: int):
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                return pedido
        
    '''
    Incluir pedido na lista.
    Tratar os casos de instancias incorretas e pedido duplicado.
    Caso o pedido já exista na lista, gerar a excecao: 
    PedidoDuplicadoException
    '''
    def incluir_pedido(self, pedido: Pedido):
        if not isinstance(pedido, Pedido):
            raise TypeError('O pedido deve ser uma instancia da classe Pedido')
        if pedido in self.__pedidos:
            raise PedidoDuplicadoException('O pedido ja existe na lista')
        self.__pedidos.append(pedido)
        
    '''
    Exclui pedido pelo numero.
    Se o pedido nao existir, deve retornar None
    Caso contrario, retorna o pedido excluido
    '''
    def excluir_pedido(self, numero: int):
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                self.__pedidos.remove(pedido)
                return pedido

    '''
    Deve calcular o total do faturamento para todos os
    itens pedidos por um CPF. 
    Recebe como parametro:
    distancia: um float que corresponde a distancia percorrida
    cpf: uma string representando o CPF do Cliente a ser faturado
    '''
    def calcular_faturamento_pedidos(self, distancia: int, cpf: str):
        total_faturado = 0
        for pedido in self.__pedidos:
            if pedido.cliente.cpf == cpf:
                total_faturado += pedido.valor_total(distancia)