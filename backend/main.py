from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['SECRET_KEY'] = 'your_secret_key'

# Mock user database
users = {
    "testuser": "testpassword"
}


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    users[username] = password
    return jsonify({'message': 'User registered successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)
