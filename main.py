import json
import pathlib

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.errorhandler(404)
def invalid_page(e):
    return 'page not exist'


def get_path():
    if app.config['TESTING']:
        return str(pathlib.Path(__file__).parent) + "/tests/testUsers.json"
    else:
        return str(pathlib.Path(__file__).parent) + '/users.json'


def read_from_file(path):
    f = open(path, 'r')
    data = json.load(f)
    f.close()
    return data


@app.route('/users')
def users_path():
    path = get_path()
    users = read_from_file(path)
    for i in users.values():
        i.pop('id')
    return ''


@app.route('/users/<username>')
def users_username_path(username):
    path = get_path()
    users = read_from_file(path)
    if username not in users.keys():
        return 'user does not exist in the database', 404
    d = {username: users[username]}
    return d


if __name__ == '__main__':
    print(pathlib.Path(__file__).parent)
    app.run(debug=True)
