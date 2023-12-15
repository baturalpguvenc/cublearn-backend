# app.py

import os
from flask import Flask, request, jsonify, session, url_for, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# MongoDB bağlantısı
client = MongoClient('mongodb://localhost:27017')
db = client['GSB_Hackatthon']
users_collection = db['users']
courses_collection = db['courses']

def load_user(wallet):
    # Kullanıcıyı yüklemek için kullanıcı koleksiyonundan veri çekme
    user_data = users_collection.find_one({"wallet": wallet})
    if user_data:
        return user_data
    return None

# Yeni endpoint'lar
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json  # JSON verisini al
    wallet = data.get('wallet')
    name = data.get('name')
    surname = data.get('surname')
    email = data.get('email')

    # MongoDB'ye ekleme işlemi
    user_data = {
        "wallet": wallet,
        "name": name,
        "surname": surname,
        "email": email
    }

    users_collection.insert_one(user_data)

    return jsonify({'message': 'User created successfully'})

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user_data = users_collection.find_one({"wallet": id})
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({'error': 'User not found'})

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.json  # JSON verisini al
    course_name = data.get('course_name')
    # Diğer gerekli course bilgilerini alabilirsiniz

    # MongoDB'ye ekleme işlemi
    course_data = {
        "course_name": course_name
        # Diğer course bilgilerini ekleyebilirsiniz
    }

    courses_collection.insert_one(course_data)

    return jsonify({'message': 'Course created successfully'})

@app.route('/courses/<id>', methods=['GET'])
def get_course(id):
    course_data = courses_collection.find_one({"course_id": id})
    if course_data:
        return jsonify(course_data)
    else:
        return jsonify({'error': 'Course not found'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
