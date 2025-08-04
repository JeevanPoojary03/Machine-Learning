from flask import Flask,render_template,request
"""
It creates an instance of the Flask class, which
will be your WSGI (Web Server Gateway Interface) application.
"""
# WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index",methods=['GET'])
def welcome1():
    return render_template('index.html')

@app.route('/about')
def about1():
    return render_template('about.html')

@app.route('/form',method=['GET','POST'])
def form():
    if request.method=='POST':
        pass
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True)