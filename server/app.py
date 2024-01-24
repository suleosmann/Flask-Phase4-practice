from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change the database URL as needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key

db.init_app(app)
CORS(app)  # Enable Cross-Origin Resource Sharing for local development

with app.app_context():
    db.create_all()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        response = {'message': 'Login successful'}
    else:
        response = {'message': 'Invalid username or password'}

    return jsonify(response)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if the username or email is already in use
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        response = {'message': 'Username or email already in use'}
        return jsonify(response), 400

    # Create a new user
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    response = {'message': 'User registered successfully'}
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)
