import os
import tempfile
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User, Location

# ---------------------------------------
# Dummy ML function
# ---------------------------------------
def predict_from_file(path):
    return "scream", 0.82


def save_location(user_id, lat, lon):
    loc = Location(user_id=user_id, latitude=str(lat), longitude=str(lon))
    db.session.add(loc)
    db.session.commit()


# ---------------------------------------
# Flask Setup
# ---------------------------------------
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shadow_guardian.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
CORS(app)


# ---------------------------------------
# REGISTER
# ---------------------------------------
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not (name and email and password):
        return jsonify({'error': 'Missing fields'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    hashed_password = generate_password_hash(password)
    user = User(name=name, email=email, password=hashed_password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Registered successfully'}), 201


# ---------------------------------------
# LOGIN
# ---------------------------------------
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    return jsonify({
        'message': 'Login success',
        'user_id': user.id,
        'name': user.name
    })


# ---------------------------------------
# AUDIO PREDICTION
# ---------------------------------------
@app.route('/api/predict_audio', methods=['POST'])
def predict_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    temp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    file.save(temp.name)

    try:
        label, score = predict_from_file(temp.name)
    finally:
        temp.close()
        os.remove(temp.name)

    return jsonify({'label': label, 'score': float(score)})


# ---------------------------------------
# LOCATION SAVE
# ---------------------------------------
@app.route('/api/update_location', methods=['POST'])
def update_location():
    data = request.json

    user_id = data.get('user_id')
    lat = data.get('latitude')
    lon = data.get('longitude')

    if not (user_id and lat and lon):
        return jsonify({'error': 'Missing fields'}), 400

    save_location(user_id, lat, lon)

    return jsonify({'message': 'Location saved'})


# ---------------------------------------
# HEALTH CHECK
# ---------------------------------------
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'Backend Connected Successfully!'})


# ---------------------------------------
# START SERVER
# ---------------------------------------
if __name__ == '__main__':
    print("🚀 Shadow Guardian Backend starting...")

    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000, debug=True)
