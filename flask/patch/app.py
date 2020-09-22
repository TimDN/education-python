import task
from task import Task
tasks = task.get_tasks()

from flask import Flask, jsonify, request, make_response
app = Flask(__name__)

def get_task(id):
    for task in tasks:
        if task.id == id:
            return task
    return None

def custom_response(message, error_code):
    return make_response(jsonify({"message": message}), error_code)

@app.route('/tasks/<int:id>', methods=["PATCH"])
def patch_task(id):
    if not request.json:
        return custom_response(f"No body in request", 400)

    task = get_task(id)
    if task is None:
        return custom_response(f"No task found with id {id}", 404)

    task.update(request.json)
    return jsonify({"task": task.to_json()})



