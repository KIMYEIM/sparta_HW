from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/update')
def update():
   return render_template('update.html')

@app.route('/songs')
def songs():
   return render_template('songlist.html')

##
@app.route('/api/update', methods=['POST'])
def api_update():
   rank_receive = request.form['rank_give']
   title_receive = request.form['title_give']
   artist_receive = request.form['artist_give']

   db.genie.update_one({'rank': rank_receive}, {'$set': {'title': title_receive, 'artist':artist_receive}})

   return jsonify({'result':'success'})

@app.route('/api/show', methods=['GET'])
def api_show():
   songs = list(db.genie.find({},{'_id': False}))

   return jsonify({'result': songs})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)