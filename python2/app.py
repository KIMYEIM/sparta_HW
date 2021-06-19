from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

#html을 주는 부분

@app.route('/')
def memo():
   return render_template('memo.html')

# Json을 주는 부분

@app.route('/api/findpw', methods=['GET'])
def test_get():
   id_receive = request.args.get('id_give')

   user = db.users.find_one({'id': id_receive}, {'_id': 0})

   if user is not None:
      return jsonify({'pw': user['pw']})
   else:
      return jsonify({'msg': '아이디가 없습니다'})



@app.route('/api/register', methods=['POST'])
def register():
   id_receive = request.form['id_give']
   pw_receive = request.form['pw_give']

   doc = {
      'id' : id_receive,
      'pw' : pw_receive
   }

   db.users.insert_one(doc)

   return jsonify({'result': 'success'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
