import os

import grpc
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

import proto_pb2
import proto_pb2_grpc

load_dotenv()

app = Flask(__name__)
cors = CORS(app)

USER_SERVICE_URL = os.getenv('USER_SERVICE_URL')
channel = grpc.insecure_channel(os.getenv('INVENTORY_SERVICE_URL'))
TRANSACTION_SERVICE_URL = os.getenv('TRANSACTION_SERVICE_URL')

artist_stub = proto_pb2_grpc.ArtistGrpcServiceStub(channel)
label_stub = proto_pb2_grpc.LabelGrpcServiceStub(channel)
record_stub = proto_pb2_grpc.RecordGrpcServiceStub(channel)

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


@app.route('/api/artists', methods=['GET'])
def get_artists():
    response = artist_stub.GetAll(proto_pb2.Empty())
    artists = []
    for artist in response:
        artists.append(from_proto(artist))
    return artists, 200


@app.route('/api/artists/<id>', methods=['GET'])
def get_artist_by_id(id):
    response = artist_stub.GetById(proto_pb2.ArtistIdProto(id=id))
    return from_proto(response), 200


@app.route('/api/labels', methods=['GET'])
def get_labels():
    response = label_stub.GetAll(proto_pb2.Empty())
    labels = []
    for label in response:
        labels.append(from_proto(label))
    return labels, 200


@app.route('/api/labels/<id>', methods=['GET'])
def get_label_by_id(id):
    response = label_stub.GetById(proto_pb2.LabelIdProto(id=id))
    return from_proto(response), 200


@app.route('/api/records', methods=['GET'])
def get_records():
    response = record_stub.GetAll(proto_pb2.Empty())
    records = []
    for record in response:
        records.append(from_proto(record))
    print(records)
    return records, 200


@app.route('/api/records/<id>', methods=['GET'])
def get_record_by_id(id):
    response = record_stub.GetById(proto_pb2.RecordIdProto(id=id))
    return from_proto(response), 200


@app.route('/api/transactions/user/<id>', methods=['GET'])
def get_transactions_of_user(id):
    response = requests.get(f'{TRANSACTION_SERVICE_URL}/transactions/user/{id}')
    return response.json(), response.status_code


@app.route('/api/transactions', methods=['POST'])
def create_transaction():
    body = request.get_json()
    if not body:
        return {'error': 'Request body is required'}, 400
    if 'userId' not in body or 'recordIds' not in body or 'totalPrice' not in body:
        return {'error': 'Not all fields provided'}, 400

    response = requests.post(f'{TRANSACTION_SERVICE_URL}/transactions', json=body)
    return jsonify({}), 201


def from_proto(proto) -> dict:
    result = {}
    for field, value in proto.ListFields():
        if isinstance(value, proto_pb2.ArtistProto) or isinstance(value, proto_pb2.RecordProto) or isinstance(value, proto_pb2.LabelProto):
            result[field.name] = from_proto(value)
        else:
            result[field.name] = value
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
