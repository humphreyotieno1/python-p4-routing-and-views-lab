#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(num) for num in range(parameter)]
    return '\n'.join(numbers) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == '/':
        return f'{num1 / num2}'
    else:
        return 'Invalid operation'
    
@app.route('/math/<int:a>/div/<int:b>')
def math_divide(a, b):
    if b == 0:
        return 'Error: Division by zero is not allowed.'
    else:
        result = a / b
        return str(result)
    
@app.route('/math/<int:a>/%/<int:b>')
def math_modulo(a, b):
    if b == 0:
        return 'Error: Division by zero is not allowed.'
    else:
        result = a % b
        return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
