"""
Nesta aula, vamos aprender sobre o próximo tipo de variável em Python, que é a tupla. 
Vamos ver que ela é muito parecida com a lista, mas com algumas diferenças importantes. 
A tupla é uma coleção ordenada e imutável de elementos. 
Isso significa que, uma vez criada, não podemos modificar seus elementos. 
Podemos criar uma tupla usando parênteses e acessar seus elementos da mesma forma que uma lista. 
Além disso, a tupla possui dois métodos úteis: 
o método count, que retorna a quantidade de vezes que um elemento aparece na tupla, 
e o método índice, que retorna o índice da primeira ocorrência de um elemento na tupla. 
Na próxima aula, continuaremos a explorar os tipos de variáveis em Python.
"""

# Criando tuplas exemplo 

tuplas = (1,2,2,2,2,3,4,5)

print("Print minha tupla", tuplas)

print("minha_tupla[0]:", tuplas[0])
print("minha_tupla[2]:", tuplas[2])
print("minha_tupla[-1]:", tuplas[-1])

# Metodo count()

contagem = tuplas.count(2)
print("A quantidade de vezes que o numero e aparece:", contagem)

indice = tuplas.index(3)
print("Indice da primeira ocorrência do elemento 3:", indice)

