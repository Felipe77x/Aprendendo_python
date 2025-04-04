"""
Nesta aula, vamos aprender sobre listas em Python. 
Uma lista é uma coleção de elementos ordenáveis e mutáveis. 
Podemos declarar uma lista usando colchetes e separando os elementos por vírgula. 
Os elementos podem ser de diferentes tipos. 
Podemos acessar os elementos da lista usando índices, que começam em 0. 
Podemos exibir a lista completa ou apenas um elemento específico usando a função print. 
Também podemos fatiar a lista, ou seja, obter um intervalo de elementos. 
Podemos fatiar do começo até um elemento específico ou a partir de um elemento específico. 
Na próxima aula, veremos sobre atribuição e os principais métodos das listas.
"""

# Declaração

lista_carro = ["Ford ka",1, "Corolla",2, "Ferrari",3, True, False]
lista_placa_car = [1112, 3334,3333,8484,9384,7438,9883,7789,8849]

# Exibindo lista

print("Minha lista de carros:", lista_carro)

# Exibindo lista

 
print("Minha lista de car", lista_carro[0])
print("Minha lista de car", lista_carro[5])
print("Minha lista de car", lista_carro[1:7])
print("Minha lista de car", lista_carro[:6])
print("Minha lista de car", lista_carro[2:])

# Principais Metodos

"""
Nesta aula, continuamos a explorar as listas em Python. 
Aprendemos sobre a parte mutável das listas e como podemos fazer alterações nos elementos. 
Demonstramos como trocar o primeiro elemento da lista por um texto usando atribuição. 
Em seguida, discutimos sobre métodos de lista, começando pelo método append, que adiciona um elemento ao final da lista. 
Em seguida, falamos sobre o método index, que retorna o índice do primeiro elemento igual ao valor especificado. 
Depois, abordamos o método insert, que insere um elemento em um índice específico. 
Em seguida, falamos sobre os métodos pop e remove, que removem elementos da lista. 
Por fim, mostramos como organizar uma lista usando o método sort. 
É importante lembrar que o método sort só funciona corretamente se todos os elementos da lista forem do mesmo tipo.

"""


# Metodo lista 


# Método append(): Adiciona um elemento ao final da lista
lista_carro.append("Supra")
print("Após append(supra)", lista_carro)

# Método index(): Informa o valor do indice da lista

indice = lista_carro.index(3)
print("Indice do elemento 6:", indice)

# Método insert: Insere um elemento em um índice específico

lista_placa_car.insert(1, 8488)
print("Após o insert(3847,8488):", lista_placa_car)


# Metodo pop(): Remove o indice do valor selecionado

elemento_removido = lista_carro.pop(3)
print("Elemento removido",elemento_removido)
print("Após o pop(3):", lista_carro)



# Metodo Remove(): Remove o valor do primeiro primeiro indice de alguma variavel

lista_carro.remove("Ferrari")
print("Após remove(Ferrari):", lista_carro)

# Metodo sort(): Lista em ordem crescente

lista_placa_car.sort()
print("Após sort()", lista_placa_car)