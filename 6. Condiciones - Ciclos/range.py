#uso del range
"""
for i in range(10): # 0 - 9
    print(i)

for i in range(5, 15): # 5 - 14
    print(i)

for i in range(0, 21, 2): # 0 - 20 de dos en dos
    print(i)
"""

#uso del enumerate
#nos devuelve un iterable que contiene tuplas donde
#el primer valor es el indice y el segundo seria el elemento
numeros = [10, 20, 30, 40, 50]
for i, numero in enumerate(numeros):
    print(i, numero)