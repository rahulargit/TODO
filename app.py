from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.todo_items

@app.route('/todo')
def todo_form():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })

    return redirect('/todo')

if __name__ == '__main__':
    app.run(debug=True)
