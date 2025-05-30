from flask import Flask, request, jsonify
from  models.task import Task


app = Flask(__name__)

#CRUD 
#Creat, Read, Update, and Delete = Criar, Ler, Atualizar e Deletar

tasks = [] 
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_tasks():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data["title"], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"menssagem": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'] )
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": task_list,
        "total_tasks": 0
            }
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
