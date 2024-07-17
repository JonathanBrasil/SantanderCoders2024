# Operações matemáticas e lógicas. 

'''

Soma: +
Subtração: -
Multiplicação: *
Divisão: /
Divisão Inteira: // (Sem os decimais)
Resto da divisão: %
Potência: **

'''


# comparações - Operadores lógicos
'''
Maior que: >
Maior ou igual: >=
Menor que: <
Menor ou Igual: <=
Igual a: = =
diferente de: !=
Obs. Para textos (str) usamos somente igual ou diferente. 
'''


x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x*y, num <= x + y, num*y != x*y)
# ==
print(num == x*y, num*y == x*y, y > x + num)

# ==================================

x = 4.2

y = 10

z = "42"

print (not (((x * y == z) and not (x < y)) or y % 2 == 0))
print(not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z)))))

