# CONDICIONAIS
'''
controle de fluxo padrao
linha abaixo de linha
'''


# IF ELIF ELSE
'''
estrutura de if:
if - condição se verdadeira:
    ação dentro do recuo...

elif - no lugar de else if

else

while = enquanto
'''

media = 10
if media>=7:
    print('aprovado')

elif media>=5:
    print('recuperacao')

else:
    print('reprovado')

# atendendo duas condições = if AND
# atendendo uma das duas condições = if OR

media = 10
presenca = 100

if media>=7 and presenca>=75:
    print('aprovado')

elif media>=5 and presenca>=75:
    print('recuperacao')

else:
    print('reprovado')