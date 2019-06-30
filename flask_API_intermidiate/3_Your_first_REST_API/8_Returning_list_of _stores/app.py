from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        "name":"My wonderful Store",
        "items":[
            {
                "name":"my item",
                "price": 19.99
            }
        ]
    }
]
#Think I'm a server.
#POST - Used to receive data
#GET - Used to send data back only

#POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

#GET /store/<string:name>
@app.route('/store/<string:name>') #,methods=['POST']
def get_store(name):
    pass

#GET /store/
@app.route('/store') #,methods=['POST']
def get_stores():
    return jsonify({"stores":stores})

#POST /store/<string:name>/item {name: , price:}
@app.route('/store/<string:name>/item', methods=['POST']) #,methods=['POST']
def create_item_in_store(name):
    pass

#POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST']) #,methods=['POST']
def get_items_in_store(name):
    pass


if __name__ == '__main__':
    app.debug=True
    app.run()
