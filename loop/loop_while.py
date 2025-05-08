# loop while

"""
Nesta aula, vamos aprender sobre o loop while em Python. 
O while é usado para repetir um bloco de código enquanto uma condição for verdadeira. 
Vamos começar com um exemplo simples, onde temos um contador que começa em 0 e é incrementado a cada iteração do loop. 
O loop continua enquanto o contador for menor que 5. 
Também podemos usar o break para sair do loop em determinada condição. 
Em seguida, vamos aplicar o while em um projeto prático, criando um menu para um gerenciador de lista de tarefas. 
O loop while será usado para repetir o menu até que o usuário escolha a opção de sair.
"""
    
While True:
    nome_cadastro = input("Digite seu nome completo.")
    if nome_cadastro > 15:
        nome_cadastro = 5 
        break
    else:
        print("Finalizar projeto")
    