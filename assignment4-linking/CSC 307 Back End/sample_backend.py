from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from uuid import uuid4

app = Flask(__name__)
CORS(app)

users = {
    'users_list':
    [
        {
            'id': 'xyz789',
            'name' : 'Charlie',
            'job': 'Janitor',
        },
        {
            'id': 'abc123',
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id': 'ppp222',
            'name': 'Mac',
            'job': 'Professor',
        },
        {
            'id': 'yat999',
            'name': 'Dee',
            'job': 'Aspiring actress',
        },
        {
            'id': 'zap555',
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        if search_username and search_job:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username and user['job'] == search_job:
                    subdict['users_list'].append(user)
            return subdict
        elif search_username:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        elif search_job:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['job'] == search_job:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = str(uuid4())
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True, user=userToAdd)
        resp.status_code = 201
        return resp


@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    return user
            return ({})
        return users
    elif request.method == 'DELETE':
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    users['users_list'].remove(user)
                    resp = jsonify(success=True)
                    resp.status_code = 204
                    return resp
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
