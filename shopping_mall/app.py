from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('shopping.html')

@app.route('/api/order', methods=['POST'])
def api_save():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    doc = {
        'name': name_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'number': number_receive
    }

    db.customers.insert_one(doc)

    return jsonify({'result': 'success'})

@app.route('/api/show', methods=['GET'])
def api_show():
    all_customers = list(db.customers.find({},{'_id':0}))

    return jsonify({'result':'success', 'customers' : all_customers})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)