#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)  # Print the route to console
    return route  # Return the route as a response

@app.route('/count/<int:number>')
def count(number):
    if number > 10:
        return '\n'.join(str(n) for n in range(10)) + '\n...'
    else:
        return '\n'.join(str(n) for n in range(number)) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        'div': lambda a, b: a / b,
        '%': lambda a, b: a % b
    }

    if operation in operations:
        return str(operations[operation](num1, num2))
    else:
        return 'Operation not recognized. Please use one of the following: + - * div %'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
