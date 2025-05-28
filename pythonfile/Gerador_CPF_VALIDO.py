

import random

cpf=""

for i in range(9):
    cpf += str(random.randint(0,9))

fatiamento = cpf[:9]
contador1 = 10
resultado1 = 0

for digito1 in fatiamento:
    resultado1 += int(digito1) * contador1
    contador1 -= 1

digito1 = (resultado1*10)%11
digito1 = digito1 if digito1 <=9 else 0

contador2 = 11
resultado2 = 0

for digito2 in fatiamento:
    resultado2 += int(digito2) *contador2
    contador2 -=1

final =  (resultado2+(digito1*2))
digito2 = (final*10)%11
digito2 = digito2 if digito2 <=9 else 0

cpffinal = str(fatiamento)+str(digito1)+str(digito2)
print(cpffinal)






