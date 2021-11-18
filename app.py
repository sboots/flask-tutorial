# app.py

# Thanks to
# https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
from flask import Flask, render_template, request
from mixpanel import Mixpanel
import os

# Additional tutorials
# https://code.visualstudio.com/docs/python/tutorial-flask
# https://pythonspot.com/flask-web-app-with-python/

app = Flask(__name__)

# Mixpanel init
# https://developer.mixpanel.com/docs/python
mp = Mixpanel(os.getenv("MIXPANEL_TOKEN"))


# home route


@app.route("/")
def hello():
    environment = os.getenv('FLASK_ENV')
    # sending a variable to the template
    return render_template('index.html', name='form tester', environment=environment)

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

    user_id = request.form['name']
    purchases = request.form['purchases']
    mp.track(user_id, 'Form submitted', {
        'purchases': purchases
    })
    return render_template('form-complete.html')


if __name__ == "__main__":
    app.run(debug=True)
