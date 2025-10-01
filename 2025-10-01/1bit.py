import sys
#195 89  
n1=195
n2=89

print(f'\n{n1} em binario é{bin(n1)}')
print(f'\n{n2} em binario é{bin(n2)}')
#operacaoes bit a bit 
print(f'\n#operacaoes bit a bit  entre {n1} e {n2}')
print(f'\t{n1} & {n2} = {n1 & n2} e em binario = {bin(n1 & n2)}')#and
print(f'\t{n1 }| {n2} = {n1 | n2}')#or
print(f'\t{n1 }^ {n2} = {n1 ^ n2}')#xor

'''do professor:
 
# Recapitulando
intValor_1 = 195
intValor_2 = 89

print(f'Valor 1................: {intValor_1:>3} -> {intValor_1:08b}')
print(f'Valor 2................: {intValor_2:>3} -> {intValor_2:08b}')

print(f'intValor_1 & intValor_2: {intValor_1 & intValor_2:>3} -> {(intValor_1 & intValor_2):08b}')
print(f'intValor_1 | intValor_2: {intValor_1 | intValor_2:>3} -> {(intValor_1 | intValor_2):08b}')
print(f'intValor_1 ^ intValor_2: {intValor_1 ^ intValor_2:>3} -> {(intValor_1 ^ intValor_2):08b}')
'''