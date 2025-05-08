"""
Nesta aula, vamos falar sobre os pilares da Programação Orientada a Objetos: abstração, encapsulamento, herança e polimorfismo. Esses conceitos são estratégias importantes para manipular classes e utilizar o paradigma da Programação Orientada a Objetos de forma eficiente. Vamos começar falando sobre herança, que é um dos pilares mais importantes. Através da herança, podemos criar classes que herdam atributos e métodos de uma classe mãe. Vou dar um exemplo de herança utilizando a classe Animal, onde podemos criar subclasses como Cachorro e Gato, que herdam os atributos e métodos da classe Animal, mas podem ter comportamentos específicos, como emitir sons diferentes. Além disso, vamos falar sobre o polimorfismo, que nos permite utilizar o mesmo método de forma diferente em diferentes classes derivadas. O polimorfismo é muito utilizado na Programação Orientada a Objetos.
"""


"""
Nesta aula, vamos falar sobre os pilares da Programação Orientada a Objetos: abstração, encapsulamento, herança e polimorfismo. Esses conceitos são estratégias importantes para manipular classes e utilizar o paradigma da Programação Orientada a Objetos de forma eficiente. Vamos começar falando sobre herança, que é um dos pilares mais importantes. Através da herança, podemos criar classes que herdam atributos e métodos de uma classe mãe. Vou dar um exemplo de herança utilizando a classe Animal, onde podemos criar subclasses como Cachorro e Gato, que herdam os atributos e métodos da classe Animal, mas podem ter comportamentos específicos, como emitir sons diferentes. Além disso, vamos falar sobre o polimorfismo, que nos permite utilizar o mesmo método de forma diferente em diferentes classes derivadas. O polimorfismo é muito utilizado na Programação Orientada a Objetos.


"""

#herança poo

class animal:
    def __init__(self, nome) -> None:
        self.nome = nome
     


    def andar(self):
        print(f"O animal {self.nome} andou")
        return


    def carrinho(self):
        pass

# herança e polimorfismo

class gato(animal):
    def carrinho(self):
        return "Sono"
    


"""
Nesta aula, discutimos três conceitos fundamentais: herança, polimorfismo e encapsulamento. 
Primeiro, exploramos como criar classes que herdam atributos e métodos de outras classes. 
Em seguida, vimos como usar o polimorfismo para implementar diferentes comportamentos para métodos comuns em classes diferentes. 
Por fim, abordamos o encapsulamento, que envolve o uso de atributos e métodos privados para proteger informações sensíveis e garantir a integridade dos dados. 
Demonstramos como criar uma classe de conta bancária com atributos privados e métodos para depositar, sacar e consultar o saldo. Ao testar o programa, vimos como as restrições do encapsulamento garantem a segurança dos dados.
"""
# Polimorfismo

class cachorro(animal):
    def carrinho(self):
        return "Au au"

print ("Exemplo de polimorfismo")

cat = gato(nome="MiMi")
dog = cachorro(nome="Toff")

animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome}  faz: {animal.carrinho()} ")



print("\n Exemplo de encapsulamento:")


class contaBancaria:
    def __init__(self,saldo) -> None:
        self.__saldo = saldo # atributo privado
        pass
    

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor 

    def consultar_saldo(self):
        return self.__saldo
    
conta = contaBancaria(saldo= 10000)

print(f"Saldo da conta bancária:{conta.consultar_saldo()}")

conta.depositar(valor=5000)

print(f"Saldo da conta bancária: {conta.consultar_saldo()}")


conta.sacar(valor=7000)

print(f"Saldo da conta bancátia: {conta.consultar_saldo()}")

conta_do_Felipe_Dias = contaBancaria(saldo = 1000)





    

    