"""
Nesta aula, aprendemos a criar uma aplicação Flask. Começamos importando a biblioteca Flask e criando uma instância da classe Flask para nossa aplicação. Em seguida, definimos uma rota chamada "/hello-world" que retorna uma string em formato HTML. Utilizamos o método run para executar o servidor localmente, com a opção debug ativada para visualizar informações de depuração. Acessamos a rota no navegador e vimos o texto "/hello-world" sendo exibido. Também criamos uma segunda rota chamada "sobre" que retorna a string "página sobre". 
Aprendemos sobre códigos de resposta HTTP, como o 200 que indica uma resposta bem-sucedida. 
Na próxima aula, continuaremos a explorar o Flask.
"""

from flask  import Flask

app = Flask (__name__)

@app.route("/")
def primeira_api():
    return " Felipe Dias estude, pois senão seu futuro vai ser triste." 



@app.route("/about")
def about():
  return "Página sobre"

if __name__ == "__main__":
  app.run(debug=True)

