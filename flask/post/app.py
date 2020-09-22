import task
from task import Task
tasks = task.get_tasks()

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

def create_task(task_dict):
    return Task(len(tasks), task_dict["title"],task_dict.get("assigned_to", ""),
     task_dict.get("completed", False), task_dict.get("description", ""))

@app.route('/tasks', methods=["POST"])
def add_task():
    # tasks must have a title. request.json contains the body of the request
    if not request.json or not 'title' in request.json:
        # 400 is returned when something was wrong with the request
        return make_response(jsonify({"message":"title is missing"}), 400)

    new_task = create_task(request.json)
    tasks.append(new_task)
    # 201 is returned when something was "Created"
    return jsonify({"task": new_task.to_json()}), 201

