from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('memo.html')

@app.route('/api/save', methods=['POST'])
def api_save():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']
    comment = comment_receive

    doc = {
        'title': title,
        'image': image,
        'desc': desc,
        'url': url_receive,
        'comment': comment
    }

    db.articles.insert_one(doc)

    return jsonify({'result':'success'})

@app.route('/api/show', methods=['GET'])
def api_show():
    all_articles = list(db.articles.find({},{'_id':0}))

    return jsonify({'result':'success', 'articles' : all_articles})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)

