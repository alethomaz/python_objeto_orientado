from pessoa import Pessoa
from cliente import Cliente
from vendedor import Vendedor


uma_pessoa = Pessoa(12312, "Ale")
um_cliente = Cliente('Av madre', 76346734, "João")
um_vendedor = Vendedor(2342, 672367234, "Pedro")

print(f"Pessoa: {uma_pessoa.nome}, CPF: {uma_pessoa.cpf} ")
print(f"Cliente: {um_cliente.nome}, endereço: {um_cliente.endereco}, CPF: {um_cliente.cpf}")
print(f"Vendedor: {um_vendedor.nome}, CPF: {um_vendedor.cpf}, comissão: {um_vendedor.comissao}")

print("Pessoa: ", uma_pessoa.  cpf)