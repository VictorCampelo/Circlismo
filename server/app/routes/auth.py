import os
import sqlite3
from flask import Blueprint, request, jsonify, g
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

# Function to get SQLite connection
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('users.db')
        g.db.row_factory = sqlite3.Row
    return g.db

# Function to close SQLite connection
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Function to initialize SQLite database with schema script
def init_db():
    db = get_db()
    with open(os.path.join('server', 'app', 'schemas', '01-init-database.sql'), 'r') as f:
        sql_script = f.read()
        cursor = db.cursor()
        cursor.executescript(sql_script)
        db.commit()


# Initialize SQLite database
init_db()

# Route for user registration
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Both username and password are required'}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400

    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    db.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# Route for user login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Both username and password are required'}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    if not user:
        return jsonify({'error': 'Invalid username or password'}), 401

    # Create JWT token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# Route for user logout (dummy implementation)
@auth_bp.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    # Dummy logout logic (clear session, token, etc.)
    username = get_jwt_identity()
    return jsonify({'message': f'User {username} logged out successfully'}), 200

# Register close_db function to close SQLite connection after each request
auth_bp.teardown_appcontext(close_db)
