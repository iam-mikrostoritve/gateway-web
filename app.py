import os

import requests
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
cors = CORS(app)

USER_SERVICE_URL = os.getenv('USER_SERVICE_URL')



@app.route('/', methods=['GET'])
def health_check():
    return {'Status': 'Running'}, 200


@app.route('/api/login', methods=['POST'])
def login():
    body = request.get_json()
    if not body:
        return {'error': 'Request body is required'}, 400
    if 'email' not in body or 'password' not in body:
        return {'error': 'Email and password are required'}, 400

    response = requests.post(f'{USER_SERVICE_URL}/login', json=body)
    return response.json(), response.status_code


@app.route('/api/register', methods=['POST'])
def register():
    body = request.get_json()
    if not body:
        return {'error': 'Request body is required'}, 400
    if 'email' not in body or 'password' not in body:
        return {'error': 'Email and password are required'}, 400

    if 'first_name' not in body:
        body['first_name'] = ''
    if 'last_name' not in body:
        body['last_name'] = ''
    body['role'] = 'USER'

    response = requests.post(f'{USER_SERVICE_URL}/signUp', json=body)
    return response.json(), response.status_code


@app.route('/api/', methods=['GET'])
def get_artists():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
