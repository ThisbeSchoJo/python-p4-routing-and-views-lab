#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    num_list_string = ""
    for num in range(0, parameter):
        num_list_string += f"{num}\n"
    return num_list_string

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        # You can't return data type integer from a view
        return f"{num1+num2}"
    elif operation == "-":
        return f"{num1-num2}"
    elif operation == "*":
        return f"{num1*num2}"
    elif operation == "div":
        return f"{num1/num2}"
    elif operation == "%":
        return f"{num1%num2}"

# @app.route('/count_and_square/<int:number>')
# def count_and_square(number):
#     squared_nums_string = ""
#     for num in range(1, number+1):
#         squared_nums_string += f'{num ** 2}\n'
#     return squared_nums_string
