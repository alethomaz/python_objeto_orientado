from onibus import Onibus
from abstractOnibus import AbstractOnibus

sao_jose = Onibus(40, 0, False)
print(sao_jose.ligar())

for i in range(5):
    sao_jose.embarca_pessoa()

print(sao_jose.total_passageiros)
print(sao_jose.ligar())
print(sao_jose.desligar())