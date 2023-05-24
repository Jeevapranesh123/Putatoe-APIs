from flask import Flask, render_template, request
from lib.MySQL import get, insert
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

table = os.getenv('TABLE_NAME')
print(table)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/get-word')
def get_word():
    word = get(table)[0][1]
    return word

@app.route('/api/insert-word',methods=['POST'])
def insert_word():
    word = request.get_json()["word"]
    if insert(table, word):
        return 'Inserted word: {}'.format(word)
    
@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )
