from flask import Flask
from flask import jsonify # import jsonify

app = Flask(__name__)

@app.route('/')
def start_page():
    item = {"name":"test", "age": 10}

    return jsonify(item) # call jsonify

@app.route('/items')
def get_items():
    items = []
    item = {"id":"1", "name":"test", "age": 10}
    item_2 = {"id":"2", "name":"test", "age": 10}
    items.append(item)
    items.append(item_2)

    return jsonify(get_ok_response(items)) # call jsonify

def add_response_status(data, status, message):
    return {"status":status,"data":data, "message": message}

def get_ok_response(data):
    return add_response_status(data, "success", "")