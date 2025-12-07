# app.py
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
user = User(name=name, email=email, password=generate_password_hash(password))
db.session.add(user)
db.session.commit()
return jsonify({'message': 'Registered successfully'})


@app.route('/api/login', methods=['POST'])
def login():
data = request.json
email = data.get('email')
password = data.get('password')
user = User.query.filter_by(email=email).first()
if not user or not check_password_hash(user.password, password):
return jsonify({'error': 'Invalid credentials'}), 401
return jsonify({'message': 'Login success', 'user_id': user.id, 'name': user.name})


# ----------------- AUDIO PREDICTION -----------------
# Expecting multipart/form-data with field name 'file'
@app.route('/api/predict_audio', methods=['POST'])
def predict_audio():
if 'file' not in request.files:
return jsonify({'error': 'No file uploaded'}), 400
f = request.files['file']
# save to temp
import tempfile
tf = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
f.save(tf.name)
try:
label, score = predict_from_file(tf.name)
finally:
tf.close()
try:
os.remove(tf.name)
except Exception:
pass
return jsonify({'label': label, 'score': float(score)})


# ----------------- LOCATION -----------------
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


# ----------------- SIMPLE HEALTHCHECK -----------------
@app.route('/api/test', methods=['GET'])
def test():
return jsonify({'message': 'Backend Connected Successfully!'})


if __name__ == '__main__':
print('🚀 Shadow Guardian Backend starting...')
app.run(host='0.0.0.0', port=5000, debug=True)
