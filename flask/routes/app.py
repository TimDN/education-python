from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/items/<int:id>', methods=["GET"]) # variable section for id
def get_item(id): # all varialbes defined in variable sections must be inparameters
    item = {"id": id, "name": "test", "price": 9.9}

    return jsonify(item)

