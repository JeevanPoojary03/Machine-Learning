from flask import Flask,jsonify,request

app=Flask(__name__)

#initial data in my todo list
items = [
    {"id":1, "name": "Item 1", "description": "This is item 1"},
    {"id":2, "name": "Item 2", "description": "This is item 2"}
]

app.route('/')
def home():
    return "Welcome to the Sample To Do List app"

#GET: Retrive all the items

@app.route('/items',methods=['GET'])



if __name__=='__main__':
    app.run(debug=True)