# app.py

# Thanks to
# https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
from flask import Flask, render_template, request

# Additional tutorials
# https://code.visualstudio.com/docs/python/tutorial-flask
# https://pythonspot.com/flask-web-app-with-python/

app = Flask(__name__)
# home route


@app.route("/")
def hello():
    # sending a variable to the template
    return render_template('index.html', name='form tester')

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
    return render_template('form-complete.html')


if __name__ == "__main__":
    app.run(debug=True)
