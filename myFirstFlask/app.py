from flask import Flask
from flask import request
from markupsafe import escape
from .calculator import calculate_sum

"""
To run the application, use the flask command or python -m flask.
You need to tell the Flask where your application is with the --app option.
However, if you name it app.py or wsgi.py, you don't need to use --app.

Ways to execute:

Method 1:
$ python -m flask --app <filename> [--debug] [run] [--port <port-number>]
# run is used when app.run() is NOT present.
# if you name it app.py or wsgi.py, you don't need to use --app.

Method 2:
if app.run() is present, then you can use:
    $ python <filename>.py

run command is used to run the application with a development server,
like this one, unlike the deployment server.

Method 3:
When outside the folder where the file 'app.py' resides , execute it as an app:
$ python -m <app_folder_name>.app
"""


app = Flask(__name__)  # app is a WSGI application


@app.route('/')
def hello():
    return ('Hello, World!')


@app.route('/user/<username>')
def user(username):
    return (f'Hello {escape(username)}, this is your personal page!')


@app.route('/calculator', methods=['POST'])
def call_calculator():
    parameters = request.json
    num1, num2 = parameters['num1'], parameters['num2']
    sum = calculate_sum(num1, num2)
    return (f'Sum of {num1} and {num2} is {sum}')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
