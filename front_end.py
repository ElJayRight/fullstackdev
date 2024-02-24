from flask import Flask, jsonify, request
from sql_api import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def base():
    methods = get_data()
    response = {
        'methods': methods
    }
    return jsonify(response)


@app.route('/<method>', methods=['GET'])
def getlanguages(method):
    languages = get_data(method)
    response = {
        'languages': languages
    }
    return jsonify(response)


@app.route('/<method>/<language>', methods=['GET'])
def getdata(method, language):
    file_name = get_data(method, language)
    if not file_name:
        return 'Not Found\n', 404
    with open(file_name, 'r') as file:
        data = file.read()
    return data

@app.route('/<method>/<language>', methods=['PUT'])
def upload(method, language):
    result = "File already on server."
    data = request.get_data().decode()
    if len(data) == 0:
        result = "File is empty"
    elif not is_in_db(method, language):
        result = add_record(method, language, data)
        result = {True: 'Added file', False: 'Failed to add file'}[result]
    response = {
        'status': str(result)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)

