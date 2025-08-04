from flask import Flask
"""
It creates an instance of the Flask class, which
will be your WSGI (Web Server Gateway Interface) application.
"""
# WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask Course.This should be an amazing course.Welcome to this best course"

@app.route("/index")
def welcome1():
    return "Welcome to this index page"



if __name__=="__main__":
    app.run(debug=True)