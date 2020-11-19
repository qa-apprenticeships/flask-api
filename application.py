import flask
from flask import request, jsonify

application = flask.Flask(__name__)
application.config["DEBUG"] = True

@application.route("/hello", methods=['POST'])
def answer():
    body = request.get_json(force=True)
    name = body['name']
    return 'Hello there, %s!' % name

@application.route("/add/<int:num1>/<int:num2>", methods=['GET'])
def add(num1, num2):
    answer = num1 + num2
    return { 'num1': num1, 'num2': num2, 'answer': answer }

if __name__ == '__main__':
    application.run()