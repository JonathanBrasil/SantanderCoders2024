# ESTRUTURA DE DADOS
# > com listas
# > são como vetores

'''
Dentro de colchetes e separados por virgulas
Pode combinar diferentes tipos de dados
'''

lista = [1,2,3]
lista2 = ['jonatha', 27, 1.72, True]
listaDeListas = [lista,lista2]

'''
Indexação

para acessar elementos dessa lista
lista[-1] = Ultima posição da lista
lista[0]  = Primeira ou Posição 0 da lista
lista[1]  = Segundo ou posição 1 da lista
etc...

'''

print(lista2[-1])
print(lista2[0])
print(lista2[1])
print(lista2[2])


#SLICES

'''

Pedaços da listas
print(lista2[0:3])
-- vai printar da posição 0 até 2
print(lista2[0:4:2])
-- vai printar da posição 0 até 3, de 2 em 2
'''

print(lista2[0:3])
print(lista2[0:4])
print(lista2[0:4:2])

# Interação com laços

for cadaElemento in lista2:
    print(cadaElemento)

'''
Dessa forma o laço irá percorrer cada elemento da lista

'''

#Tamanho da lista
print(len(lista2))  #len()
print('comprimento da lista2: ',len(lista2))

#Métodos de lista

'''
Os métodos usados são:
.append() -> acrescenta um elemento ao final da lista
.insert(posição,elemento) -> acrescenta um elemento na posição escolhida da lista
.extend() -> Para juntar duas listas
.pop() -> Para remover o elemento numa posição ou o ultimo. 
.remove() -> Para remover o próprio elemento
.count() -> vai contar a quantidade de elementos igual o parâmetro
.index() -> informa qual a posição (index) do elemento informado
.sort() -> para ordenar a lista (de forma crescente padrão)
.sort(reverse=True) -> Irá ordenar de forma decrescente

len(lista) -> mostra o tamanho da lista
sum(lista) -> soma os elementos da lista
max(lista) -> mostra o maior valor(elemento) da lista
min(lista) -> mostra o menor valor(elemento) da lista

'''

listaNumeros = [0,1,2,3,4,5]
listaNumeros2 = [7,8,'excluir',90,98,30,20]
listaNumeros.append(6) #vai add 6 ao final da lista
listaNumeros.insert(2,20) #vai adicionar 20 na posição 2 da lista
listaNumeros.extend(listaNumeros2) #vai adicionar a listaNumeros2 continuando 
listaNumeros.pop(2) #vai remover o elemento que está na posição 2
listaNumeros.remove('excluir') #vai remover o elemento igual ao do parâmetro
listaNumeros.count(90) #vai contar quantas vezes o elemento do parâmetro repete
listaNumeros.index(8) #informa a posição do número 8 na lista 
listaNumeros.sort(reverse=True) #ordena de forma decrescente
sum(listaNumeros) #Soma todos os elementos da lista

print(listaNumeros)
print(min(listaNumeros))

idade = int(input('Digite sua idade:'))
if idade>=18:
    print('maior')
else:
    print('menor')


numero = int(input('digite um numero:'))
if numero>0:
    print('positivo')
elif numero == 0:
    print('nulo')
else:
    print('negativo')

numero1 = int(input('digite o primeiro numero:'))
numero2 = int(input('digite o segundo numero:'))



