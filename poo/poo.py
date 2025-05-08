import os
from  dataclasses import dataclass

os.system("cls || clear")


"""
Nesta aula, vamos mergulhar no mundo da programação orientada a objetos (POO). 
Uma linguagem de programação orientada a objetos adota e implementa os princípios e conceitos da POO. 
Essas linguagens, como Python, Java, C++, C Sharp e Ruby, permitem que os programadores criem softwares de forma modular, reutilizável e mais fácil de entender e manter. 
A POO é um paradigma de programação que se baseia na organização dos programas em torno de objetos, que são instâncias de classes. As classes são modelos que definem a estrutura e o comportamento dos objetos. 
Dentro das classes, podemos descrever atributos e métodos, que são as ações que os objetos podem realizar. O construtor é um método especial que nos permite definir os atributos da classe.

"""

# class 

class pessoa:
    def __init__(self, idade, nome  ) -> None:
        self.idade = idade
        self.nome = nome
    def sono(self):
        return f"Idade: {self.idade} Nome: {self.nome}"   

# Objeto

pessoa1 = pessoa( "Felipe Dias",  3)
mensagem = pessoa1.sono()
print(mensagem)




