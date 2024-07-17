# Laços de repetição

'''
Continuação do controle de fluxo de código no Python
while = enquanto
o código vai continuar repetindo até atender uma condição
precisando tomar cuidado com looping infinito.
(laço não controlado)

'''
# LAÇO WHILE
# continua repetindo o código enquanto o numero inserido for diferente de 15

numeroSorteado = 15
numeroUsuario = int(input('Informe um número'))

while numeroSorteado != numeroUsuario:
    print('Você errou')
    numeroUsuario = int(input('Informe um número'))

print('Acertou!')
# somente ao digitar 15 vai acabar o laço, encerrando o programa

# Ex2. com contador (repeticao controlado com while)

contador = 0
while contador < 5:
    print(contador)
    contador=contador+1

# nessa estrutura vai contar de 0 a 4
# ===================================

# LAÇO FOR

'''
Ideal quando sabemos quantas vezes o laço precisará ser repetido
Melhor forma de fluxo controlado com contador
'''

for contador in range(10):
    print(contador)

'''
O contador irá de 0 a 9
será incrementado sozinho
'''

# laço for com 2 ou 3 parametros
'''
valor inicial, valor final
ou
valor inicial, valor final, passo
'''
# irá contar de 5 a 10

for variavel in range(5,11):
    print(variavel)

# irá contar de 0 a 10 mas de 2 em 2 (passo)
#0,2,4,6,8,10
for variavel in range(0,11,2):
    print(variavel)

#Outro exemplo
for i in range(1,4):
    nota = float(input(f'Informe a sua nota de p{i}:'))
    soma = soma+nota
print(f'sua média é de {soma/3}')