"""
    Nesta aula, vamos aprender sobre o tipo de variável texto em Python. 
O Python é de tipagem dinâmica, o que significa que ele identifica o tipo de texto pela presença de aspas. 
Existem várias formas de declarar uma variável de texto, a mais simples é usando aspas duplas ou simples. 
Também é possível usar três aspas antes e depois do texto para permitir a quebra de linhas. 
Outra opção é usar a barra invertida para quebrar o texto em duas linhas. 
Recomenda-se usar aspas duplas por padrão. Além disso, vamos declarar algumas variáveis de texto, como nome completo, nome e sobrenome.
"""

# STRINGS

# DECLARAÇÃO

nome_completo = "Felipe"


nome_completo_aspas = """
Naruto

"""

nome_completo_quebra = "Felipe  \
dias"

# FORMATAÇÃO 

sobrenome = "Dias"
nome = "Dormir melhora a saude"

print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Gabriel" + "Casemiro")
print("Nome completo (4a forma):" + "Gabriel", "Casemiro")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}") 
print("Nome completo (10a forma): {} {}".format(sobrenome, nome))


# Metodos de strings

# Metodo upper

fruta = "manga"



print(fruta.upper())


# Metodo Lower 

animal = "GATO"



print(animal.lower())

# Metodo count

metodo_3 = nome.count("a")

print(metodo_3)


# Metodo find 

metodo_4 = nome.find("a")

print(metodo_4)

# Metodo encode

metodo_5 = nome.encode()

print(metodo_5)

# Metodo decode

metodo_6 = nome.encode().decode()

print(metodo_6)


# Metodo replace

metodo_7 = nome.replace("o" , "123")

print(metodo_7)


# Metodo join

metodo_8 = "-".join(nome)

print(metodo_8)

# Metodo split

metodo_9 = nome.split()

print(metodo_9)

# Metodo strip

metodo_10 = nome.strip("e"+ "D")

print(metodo_10)


# Metodo star

metodo_11 = nome.startswith("Do")

print(metodo_11)

# comparadores in e not in

# comparador in
comparador_1 = "or" in nome

print(comparador_1)
#comparador not in 

comparador_2 = "or" not in nome 

print(comparador_2)