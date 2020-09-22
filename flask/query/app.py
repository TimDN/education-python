import task
import sqlite3
import os
from distutils import util

from task import Task
tasks = task.get_tasks()

from flask import Flask, jsonify, request, make_response, url_for
app = Flask(__name__)

database_path = os.path.join(app.root_path, 'test.db')

def get_task_with_id(id):
    task = select_query_on_db("SELECT * FROM tasks WHERE id = ?", [id])
    if len(task) == 0:
        return None
    else:
        return create_task_from_db(task[0])

def custom_response(message, error_code):
    return make_response(jsonify({"message": message}), error_code)

def return_task(task):
    return jsonify({"task": make_public_task_json(task)})

def create_task(task_dict):
    return Task(len(tasks), task_dict["title"],task_dict.get("assigned_to", ""),
     task_dict.get("completed", False), task_dict.get("description", ""))

def create_task_from_db(db_task):
    return Task(db_task[0], db_task[1], completed=db_task[2])

def make_public_task_json(task):
    task = task.to_json()
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

def select_query_on_db(query, params = None):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)
        result = cursor.fetchall()
    finally:
        connection.close()
    return result

#example /tasks?completed=False
@app.route('/tasks', methods=["GET"])
def get_tasks():
    query = request.args
    if "completed" in query:
        completed = util.strtobool(query["completed"])
        db_tasks = select_query_on_db("SELECT * FROM tasks WHERE completed = ?", [completed])
    else:
        db_tasks = select_query_on_db("SELECT * FROM tasks")

    local_tasks = []
    # performs select query on database returning fetchall result
    for db_task in db_tasks:
        # create a new task object using the result from the database
        local_tasks.append(create_task_from_db(db_task))
    return jsonify({"tasks": [make_public_task_json(task) for task in local_tasks]})


@app.route('/tasks/<int:id>', methods=["GET"])
def get_task(id):
    task = get_task_with_id(id)
    if task is None:
        return custom_response(f"No task found with id {id}", 404)
    else:
        return return_task(task)