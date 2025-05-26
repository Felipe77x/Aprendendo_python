from flask import Flask, request
from  models.task import Task


app = Flask(__name__)

#CRUD 
#Creat, Read, Update, and Delete = Criar, Ler, Atualizar e Deletar

tasks = [] 

@app.route('/tasks', methods=['POST'])
def create_tasks():
    data = request.get_json()
    return 'Felipe estude bastante para sair da pobreza.'




if __name__ == "__main__":
    app.run(debug=True)
