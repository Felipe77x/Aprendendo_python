"""
Nesta aula, vamos falar sobre o Flask, um framework para desenvolvimento web em Python. O Flask é conhecido por sua simplicidade e facilidade de uso, permitindo que os desenvolvedores construam aplicações web robustas. Ele oferece liberdade aos desenvolvedores para escolher as ferramentas e abordagens durante o desenvolvimento. Alguns exemplos de empresas que utilizam o Flask são o Pinterest, LinkedIn, Netflix e Uber. Para utilizar o Flask, é necessário instalar suas dependências. Isso pode ser feito através do comando pip3 install flask no terminal ou criando um arquivo de requisitos e instalando as dependências através do comando pip install -r requirements.txt.
"""

from flask import Flask

app = Flask(__name__) 

@app.route("/")
def primerira_rota():
    return"Sucesso "

@app.route("/about")
def about():
  return "Página sobre"



if __name__ == "__main__":
  app.run(debug=True)
