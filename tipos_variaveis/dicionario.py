"""
Nesta aula, vamos aprender sobre dicionários em Python. 
Um dicionário é uma coleção não ordenada de pares chave-valor. 
Podemos criar um dicionário usando chaves e armazenar informações dentro dele. 
Cada chave é importante para acessar a informação posteriormente. 
Podemos adicionar várias chaves e valores ao dicionário, inclusive outros dicionários. 
Podemos exibir o dicionário usando a função print e acessar os valores usando as chaves. 
Se tentarmos acessar uma chave que não existe, receberemos uma exceção KeyError. 
Podemos adicionar novas chaves ao dicionário mesmo depois de criá-lo. 
Na próxima aula, aprenderemos sobre os métodos para manipular dicionários.

"""

# criando um dicionario

dicionario_pessoa = {"nome":  "Felipe", "idade": 20, "profissão": "Informatica"}

# Exibindo dicionario

print("Dicionario pessoa", dicionario_pessoa)

# Acessando valores

print("Nome:", dicionario_pessoa["nome"])

#dicionario_pessoa = {"Sobrenome": "Dias"}
 


# Metodos do dicionario



"""
Nesta aula, continuamos nossos estudos sobre dicionários em Python. 
Aprendemos como atualizar um valor existente em um dicionário, utilizando a mesma sintaxe de criação. 
Também vimos como remover um par chave-valor utilizando o comando del. 
É importante lembrar que o del exclui todo o par chave-valor, não apenas a chave ou o valor separadamente.

Em seguida, exploramos três métodos principais para manipular dicionários: keys(), values() e items(). 
O método keys() retorna todas as chaves do dicionário em formato de lista. 
O método values() retorna todos os valores do dicionário em formato de lista. 
Já o método items() retorna uma lista de tuplas contendo todos os pares chave-valor.

É importante notar que, ao utilizar o método keys(), values() ou items(), 
é necessário transformar o resultado em uma lista utilizando a função list() para acessar os elementos individualmente.

Na próxima aula, continuaremos a explorar dicionários em Python.
"""

# Removendo um par chave-valor
del dicionario_pessoa["nome"]

print("Meu dicionário de exemplo:", dicionario_pessoa)
 
 # Métodos: keys(), values(), items()

#list = {"sala":1,"sala":2 ,"sala":3,}
chaves = list(dicionario_pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])
 
 # Métodos values
valores = list(dicionario_pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])
 
 # Métodos items
itens = list(dicionario_pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))




