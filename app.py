from flask import Flask, jsonify, request, render_template

app = Flask(__name__)  # gives us information that is running in a specific unique place flask app

stores = [{
    'name': 'My wonderful store',
    'items': [{'name': 'My item', 'price': 12.99}]}]


# POST - used to receive data
# GET - used to send data back only
# The browser perspective is opposite browser used POST to send us a data, but GET to receive data

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')  # 'http://127.0.0.1:4999/store/some_name'
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})



# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'error'})


@app.route('/')  # http://www.google.com/'
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=4999)
