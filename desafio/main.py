from funcionario import Funcionario
from dependente import Dependente 
from cargo import Cargo


cargo_jr = Cargo(100, 'dev_jr')
cargo_sn = Cargo(200, 'dev_sn')

funcionario_1 = Funcionario('Ale', 12312, cargo_jr)
funcionario_2 = Funcionario('Joao', 12312, cargo_sn)
funcionario_3 = Funcionario('Ian', 21313, cargo_jr)

funcionario_1.add_dependente('dep 1', 12121)
funcionario_2.add_dependente('dep 2', 1121)

print(cargo_jr)
print(cargo_sn)
print(funcionario_1)
print(funcionario_2)
