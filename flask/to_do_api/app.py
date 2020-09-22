import task
import sqlite3
import os

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

def insert_task_into_db(cursor, task):
    insert_query = "INSERT INTO tasks VALUES(null, ?, ?)"
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute(insert_query, [task.title, task.completed])
        connection.commit()
    except:
        connection.rollback()
    finally:
        connection.close()
    return result

# not using DB
@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
    task = get_task_with_id(id)
    if task is None:
        return custom_response(f"No task found with id {id}", 404)
    tasks.remove(task)
    return jsonify({"result": True})

# not using DB
@app.route('/tasks/<int:id>', methods=["PATCH"])
def patch_task(id):
    if not request.json:
        return custom_response(f"No body in request", 400)

    task = get_task_with_id(id)
    if task is None:
        return custom_response(f"No task found with id {id}", 404)

    task.update(request.json)
    return return_task(task)

@app.route('/tasks', methods=["GET"])
def get_tasks():
    query = request.args
    if "completed" in query:
        completed = util.strtobool(query["completed"])
        db_tasks = select_query_on_db("SELECT * FROM tasks WHERE completed = ?", [completed])
    else:
        db_tasks = select_query_on_db("SELECT * FROM tasks")

    local_tasks = []
    for db_task in db_tasks:
        local_tasks.append(create_task_from_db(db_task))
    return jsonify({"tasks": [make_public_task_json(task) for task in local_tasks]})

@app.route('/tasks/<int:id>', methods=["GET"])
def get_task(id):
    task = get_task_with_id(id)
    if task is None:
        return custom_response(f"No task found with id {id}", 404)
    else:
        return return_task(task)

@app.route('/tasks', methods=["POST"])
def add_task():
    if not request.json or not 'title' in request.json:
        return make_response(jsonify({"message":"title is missing"}), 400)

    new_task = create_task(request.json)
    insert_task_into_db(new_task)
    return return_task(new_task), 201

if __name__ == "__main__":
    main()