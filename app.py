from flask import Flask, request, jsonify
import json
from flask_restful import Resource, Api
from flask_cors  import CORS
from costs import *
import pickle
from index_generating import *


app = Flask(__name__)

api = Api(app)


@app.route('/')
def index():
    return 'Welcome to fepco ^_^'


################ Town Cost Get and Post ##############

@app.route('/town/<cost_id>&<cost_amount>', methods=['GET'])
def get_town_cost(cost_id, cost_amount):

    town_data = {
        'cost_id' : cost_id,
        'cost_amount' : cost_amount,
    }

    id = int(town_data['cost_id'])
    cost_amount = int(town_data['cost_amount'])
    
    obj = TownCost(id, cost_amount)
    with open('data_file.pkl', 'ab') as f:
        pickle.dump(obj, f)
    
    return jsonify(town_data), 200




@app.route('/town/post', methods=['POST'])
def post_town_cost():

    data = request.get_json()
    amount = int(data['amount'])
    id = int(data['id'])
    obj = TownCost(id, amount)

    with open('data_file_post.pkl', 'ab') as f:
        pickle.dump(obj, f)

    return jsonify(data), 201


#################### GET and POST for Block ###

@app.route('/block/<cost_id>&<cost_amount>', methods=['GET'])
def get_block_cost(cost_id, cost_amount):

    block_data = {
        'cost_id' : cost_id,
        'cost_amount' : cost_amount,
    }

    id = int(block_data['cost_id'])
    cost_amount = int(block_data['cost_amount'])
    
    obj = BlockCost(id, cost_amount)
    with open('data_file.pkl', 'ab') as f:
        pickle.dump(obj, f)
    
    return jsonify(block_data), 200




@app.route('/block/post', methods=['POST'])
def post_block_cost():

    data = request.get_json()
    amount = int(data['amount'])
    id = int(data['id'])
    obj = BlockCost(id, amount)

    with open('data_file_post.pkl', 'ab') as f:
        pickle.dump(obj, f)

    return jsonify(data), 201



####################### GET and POST for Floor ###

@app.route('/floor/<cost_id>&<cost_amount>', methods=['GET'])
def get_floor_cost(cost_id, cost_amount):

    floor_data = {
        'cost_id' : cost_id,
        'cost_amount' : cost_amount,
    }

    id = int(floor_data['cost_id'])
    cost_amount = int(floor_data['cost_amount'])
    
    obj = FloorCost(id, cost_amount)
    with open('data_file.pkl', 'ab') as f:
        pickle.dump(obj, f)
    
    return jsonify(floor_data), 200



@app.route('/floor/post', methods=['POST'])
def post_floor_cost():

    data = request.get_json()
    amount = int(data['amount'])
    id = int(data['id'])
    obj = FloorCost(id, amount)

    with open('data_file_post.pkl', 'ab') as f:
        pickle.dump(obj, f)

    return jsonify(data), 201

####################### GET and POST for Unit ###

@app.route('/unit/<cost_id>&<cost_amount>', methods=['GET'])
def get_unit_cost(cost_id, cost_amount):

    if not(int(cost_id) in unit_index()):
        return "id is not valid."
    
    unit_data = {
        'cost_id' : cost_id,
        'cost_amount' : cost_amount,
    }

    cost_amount = int(unit_data['cost_amount'])
    
    obj = UnitCost(cost_amount)
    with open('my_json_get_data.json', 'r+') as file:
        content = json.load(file)
        # obj_value = json.dumps(obj.__dict__)
        content["cost_id"].append(obj.__dict__)
        file.seek(0)
        json.dump(content, file, indent=4)
    
    return jsonify(unit_data), 200



@app.route('/unit/post', methods=['POST'])
def post_unit_cost():

    data = request.get_json()
    amount = int(data['amount'])
    id = int(data['id'])
    obj = UnitCost(id, amount)

    with open('data_file_post.pkl', 'ab') as f:
        pickle.dump(obj, f)

    return jsonify(data), 201



if __name__ == '__main__':
    app.run(debug=True, port=8080)
