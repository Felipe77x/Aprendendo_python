"""
Nesta aula, vamos falar sobre o conceito de abstração na programação orientada a objetos. 
A abstração é um conceito importante que nos permite criar um molde para construir classes. 
Uma classe abstrata não pode ser instanciada diretamente, mas serve como um modelo para outras classes. 
Isso nos ajuda a proteger as características, como atributos e métodos, que uma classe deve ter. 
No Python, podemos usar o pacote ABC para criar classes abstratas. 
Ao criar uma classe derivada, é obrigatório implementar os métodos definidos na classe abstrata. 
Isso nos permite ter segurança e consistência no código, mesmo quando trabalhamos com diferentes classes derivadas. 
A abstração é especialmente útil ao lidar com bancos de dados, pois nos permite criar classes genéricas que podem ser facilmente adaptadas para diferentes tipos de bancos de dados.
"""


print("\n Exemplos de abstração")

from abc import ABC, abstractmethod

class estudante(ABC):
    @abstractmethod

    def estudar(self):
        pass

    def leitura(self):
        pass



class estudante_matematica(estudante):
    def __init__(self, ) -> None:
        pass

    def estudar(self):
        return "O horário para estudar todos os dias é 08:00 ás 12:00 da manhã !!!"
    
    def leitura(self):
        return "A leitura tem que ser um hábito habitual, ou seja,  ler todos os dias um pouco"


estudantes = estudante_matematica()
print(estudantes.leitura())
print(estudantes.estudar())



