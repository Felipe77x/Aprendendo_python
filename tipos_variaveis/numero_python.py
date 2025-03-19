"""
      Nesta aula, vamos aprofundar nossos conhecimentos sobre o primeiro tipo de variável em Python: os números. 
Vamos aprender sobre os tipos de números disponíveis, começando pelo inteiro. 
Para declarar uma variável inteira, basta atribuir um número inteiro a ela. 
Em seguida, vamos falar sobre os números reais com ponto flutuante, que são utilizados quando precisamos lidar com valores quebrados, como dinheiro. 
Vamos criar um programa para imprimir os valores das variáveis inteira e real, utilizando a função print. 
Também vamos aprender sobre a função type, que retorna o tipo da variável. 
Ao executar o programa, veremos que o tipo da variável inteira é int e o tipo da variável real é float. 

"""
# tipo int

inteiro = 20

# tipo float

decimal  = 100.00

# A classe  type() retornar o tipo da variavel

print(f"O valor da variavel = {type(inteiro)}")
print(f"O valor da variavel = {type(decimal)}")


# operações aritméticas

# SOMA

soma = 5 + 5
print(f"O valor {soma}")

# subtração 

subtracao = 5 - 5
print(f"O valor {subtracao}")

# MULTIPLICAÇÃO 

multiplicacao = 5 * 5
print(f"O valor {multiplicacao}")

# DIVISÃO 

divisao = 5 / 5
print(f"O valor {divisao}")

# RESTO DA DIVISÃO

resto = 8 % 7
print(f"O valor {resto}")
