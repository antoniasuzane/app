from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

LIVROS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'autor': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'autor': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'autor': 'Dr. Seuss',
        'read': True
    }
]


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/biblioteca', methods=['GET', 'POST'])
def all_livros():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        LIVROS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'autor': post_data.get('autor'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Livro adicionado!'
    else:
        response_object['livros'] = LIVROS
    return jsonify(response_object)

@app.route('/biblioteca/<livro_id>', methods=['PUT', 'DELETE'])
def single_livro(livro_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_livro(livro_id)
        LIVROS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'autor': post_data.get('autor'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Livro atualizado!'
    if request.method == 'DELETE':
        remove_livro(livro_id)
        response_object['message'] = 'Livro removido!'
    return jsonify(response_object)


def remove_livro(livro_id):
    for livro in LIVROS:
        if livro['id'] == livro_id:
            LIVROS.remove(livro)
            return True
    return False

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()