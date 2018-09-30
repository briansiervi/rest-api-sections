from flask import Flask, jsonify, request

app = Flask(__name__)

stores =[
    {
        'name': 'Test',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]

# In a webserver (not in browser)
# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string: name>
@app.route('/store/<string:name>')
def get_store(name):
    store = list(filter(lambda x: x['name'] == name, stores))
    if len(store) > 0:
        return jsonify({'store': store})
    else:
        return jsonify({'message':'Store {} not found'.format(name)})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    store = list(filter(lambda x: x['name'] == name, stores))
    if len(store) > 0:
        return jsonify({'items': store['items']})
    else:
        return jsonify({'message':'Store {} not found'.format(name)})

app.run(port=5000, debug=True)