from funcionario import Funcionario
from caixa import Caixa
from vendedor import Vendedor 
from traine import Trainee

#funcionario_1 = Funcionario(3636723, 1000)
caixa_1 = Caixa(7373, 1000.00, 200.00)
print('Caixa de CPF: ', caixa_1.cpf)
print('Salário: ', caixa_1.salario_total())

print('-='*40)

vendedor_1 = Vendedor(12312, 1000.00, 100.00, 20.00)
print('Vendedor de CPF: ', vendedor_1.cpf)
print('Salário: ', vendedor_1.salario_total())

# Definindo um método genérico para calcular os valores totais dos salários 

def salarios_totais(funcionarios):
  total = 0
  for funcionario in funcionarios:
    print('Salario total:', funcionario.salario_total(), 'do funcionario:', funcionario.cpf)
    total += funcionario.salario_total()
  print('>>> Valor total dos salarios:', total)

# Instanciando uma lista com os funcionários:

caixa1 = Caixa(12312, 1000.0, 250.0)
caixa2 = Caixa(312321, 1200.0, 230.0)
vendedor1 = Vendedor(1231, 1500.00, 5.0, 10000.00)
vendedor2 = Vendedor(126216, 1500.00, 5.0, 10000.00)

funcionarios = []
funcionarios.append(caixa1)
funcionarios.append(caixa2)
funcionarios.append(vendedor1)
funcionarios.append(vendedor2)

# Calculando o salário de todos:

salarios_totais(funcionarios)

trainee1 = Trainee(12331, 1000.00)
trainee2 = Trainee(21313, 1000.00)

funcionarios.append(trainee1)
funcionarios.append(trainee2)

salarios_totais(funcionarios)
