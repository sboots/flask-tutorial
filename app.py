# app.py

# Thanks to
# https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
from flask import Flask, render_template, request

app = Flask(__name__)
# home route
@app.route("/")
def hello():
    return render_template('index.html', name = 'John')  # sending a variable to the template

# serving form web page
@app.route("/my-form")
def form():
    return render_template('form.html')

# handling form data
@app.route('/form-handler', methods=['POST'])
def handle_data():
    # since we sent the data using POST, we'll use request.form
    print('Name: ', request.form['name'])
    # we can also request.values
    print('Purchases: ', request.form['purchases'])
    return "Request received successfully!"

app.run(debug = True) 
