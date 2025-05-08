"""
Nesta aula, vamos aprender sobre loops em programação. 
Os loops são estruturas que nos permitem repetir um bloco de código enquanto uma condição for verdadeira. 
Existem dois tipos de loops: o "for" e o "while". Nesta aula, vamos focar no loop "for". 
O loop "for" é utilizado para iterar sobre uma sequência de elementos, como listas, tuplas e dicionários. 
Vamos começar vendo como o loop "for" funciona com listas. Em seguida, veremos como utilizá-lo com tuplas e dicionários. 
Com dicionários, podemos imprimir as chaves, os valores ou ambos juntos. 
Vamos explorar esses conceitos e exemplos na aula.
"""


print("For utilizando lista")
lista_numerica = [1,2,3,4,5] 

for i in lista_numerica:
    print(i)

print("For utilizando tupla")

tuplas = (1,2,3,4,5)

for tupla in tuplas:
    print(tupla)


lista_numericas = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("For utilizando dicionatio - chaves")
for chave in lista_numericas.keys():
   print(chave)


print("\nFor utilizando dicionatio - valores")
for valor in lista_numericas.values():
   print(valor)
 
print("\nFor utilizando dicionatio - items")
for chave, valor in lista_numericas.items():
   print(f"{chave}: {valor}")


"""
Nesta aula, vamos explorar alguns truques para utilizar junto com o loop for. 
O primeiro truque é a função range, que retorna um intervalo numérico em formato de lista. 
Podemos usar o range para criar listas de forma mais rápida, em vez de declarar manualmente cada elemento. 
Também podemos usar a função length em conjunto com o range para obter a quantidade de elementos em uma lista. 
Outra função útil é a enumerate, que permite extrair tanto o valor quanto o índice de cada elemento de uma lista. 
Essas funções são muito utilizadas em programação e é importante saber quando e como utilizá-las.
"""

print("\n Utilizando a função range()")
lista_numero = [1,2,3,4,5,6,7,8,9,10]

for lis_num in range(10):
   print(lis_num)

for i  in range(20):
   print(i)

print("\n Utilizando a função range() com len()")

lista_nome = ["Felipe","Dias", "Marcos"]

for indice in range(0, len(lista_nome)):
   print("Indice", indice)
   print("Elemento:", lista_nome[indice])

   if indice == 2:
      lista_nome[indice] = "Felipe"
   else:
      lista_nome[indice] = "Felipe Dias"
      print(lista_nome)


print("enumerate()")
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
   print(f"{indice}: {valor}")
   if indice == 1:
     print("Idice 1")