from flask import Flask, send_from_directory
from flask import request
from json import dumps

app = Flask(__name__)

@app.route('/<path:path>')
def main_pages(path):
    return send_from_directory('', path)

class some_class:
    def __init__(self):
        self.value1 = 1
        self.value2 = 2

@app.route('/some_class')
def show_class():
    return dumps(some_class().__dict__)

@app.route('/some_class/<id>/stuff')
def with_an_id(id):
    c = some_class()
    c.id = id
    return dumps(c.__dict__)

if __name__ == '__main__':
    print(show_class())
    print(with_an_id(123))

