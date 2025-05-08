""""
Nesta aula, vamos falar sobre entrada de dados em programas. 
A entrada de dados permite que o programa interaja com o usuário, permitindo que ele digite valores no terminal. 
Para isso, podemos utilizar a função input(), onde podemos fazer uma pergunta ao usuário e armazenar a resposta em uma variável. 
Por exemplo, podemos perguntar a idade do usuário e usar essa informação para tomar decisões no programa. 
É importante lembrar que o valor digitado pelo usuário será armazenado como uma string, então, se precisarmos comparar com números, devemos converter para inteiro usando a função int(). 
Dessa forma, podemos criar programas mais interativos e intuitivos.
"""

# if, elif e else
 
 # Exemplo de "if"
idade = 18
idade = int(input("Quantos anos você tem? "))
print("Exemplo de comando if")
if idade >= 18:
   print("Você é maior de idade.")