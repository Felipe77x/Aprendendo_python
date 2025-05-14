"""
Nesta aula, vamos falar sobre herança múltipla. 
Vamos entender o que é herança múltipla e como podemos utilizá-la em nossos programas. 
Começaremos criando um arquivo chamado "herança-múltipla.py". 
Em seguida, mostrarei um exemplo de herança comum, onde criaremos uma classe "animal" com métodos e atributos comuns a todos os animais. 
Em seguida, criaremos classes filhas para herdar esses métodos e atributos. Por exemplo, criaremos a classe "mamífero" que herdará de "animal" e terá a habilidade de amamentar. 
Também criaremos a classe "ave" que herdará de "animal" e terá o método "voar". 
Em seguida, mostrarei como fazer herança múltipla, onde criaremos a classe "morcego" que herdará tanto de "mamífero" quanto de "ave". 
Para implementar a herança múltipla, usaremos uma vírgula para separar as classes que queremos herdar. 
Também mostrarei como implementar métodos específicos para a classe "morcego" usando a função "super". 
Por fim, faremos alguns testes para verificar se tudo está funcionando corretamente. 
A herança múltipla nos permite herdar de várias classes diferentes e ter acesso a todos os métodos e atributos em cadeia.
"""


class gato:
    def __init__(self, nome, raca) -> None:
        self.nome  = nome
        self.raca = raca



    def pular(self):
        pass


class gato_amarelo(gato):

    def emitir_som(self):
        return " MIAU"

    def pular(self):
        return f"O NOME DO GATO É {self.nome} E A RACA {self.raca}"
       


class gato_preto(gato):
    def correr(self):
        return f"Corre atras dos ratos {self.nome} da raça {self.raca}"



class mae_gato( gato_amarelo, gato_preto):
    def emitir_som(self):
        return "miau"

gatos = mae_gato(nome="Batman", raca = "Felino")

# Acessando métodos da classe base `Animal`
print("Nome do morcego:", gatos.nome)
print("Som do morcego:", gatos.emitir_som())

# Acessando métodos das classes `Mamifero` e `Ave`
print("Morcego amamentando:", gatos.pular())
print("Morcego voando:", gatos.correr())

