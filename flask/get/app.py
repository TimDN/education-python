import task
from task import Task
tasks = task.get_tasks()

from flask import Flask, jsonify, make_response
# make response allows use to create custom responses

app = Flask(__name__)

@app.route('/tasks', methods=["GET"])
def get_tasks():
    return jsonify([task.to_json() for task in tasks])

@app.route('/tasks/<int:id>', methods=["GET"])
def get_task(id):
    result = None
    for task in tasks:
        if task.id == id:
            result = task
            break
    if result is None:
        return make_response(jsonify(f"Task with id {id} not found"), 404)
        # using make_response to return error
    else:
        return jsonify(result.to_json())
