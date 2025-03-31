"""
Nesta aula, vamos aprender sobre o tipo booleano em programação. 
Os booleanos são variáveis que podem ter apenas dois valores: true (verdadeiro) ou false (falso). 
Eles são amplamente utilizados em todas as linguagens de programação, principalmente em comparações e condicionais. 
Nas condicionais, temos blocos de código que são executados se uma determinada condição for verdadeira. 
Podemos utilizar os operadores lógicos "and" e "or" para comparar duas entradas e obter uma saída. 
O operador "and" só retorna verdadeiro se as duas condições forem verdade
"""
# condição verdadeira 

True

#condição falsa

False


# se condição

# se nao = else

if True:
    print("O bloco IF vai ser executado.")
else:
    print("Bloco ELSE não será executado")

# Operadores lógicos: and e or
 
 # AND  
if True and True:
   print("Bloco será executado")
 
elif True and False: 
   print("Bloco não será executado")
 
elif False and False:
   print("Bloco não será executado")
else:
   print("ok")
   
 # OR
if True or False:
   print("Bloco OR vai ser executado")
 
elif False or False:
   print("Bloco OR não vai ser executado")
 
elif True or True:
   print("Bloco OR vai ser executado")
else: 
   print("ok")

