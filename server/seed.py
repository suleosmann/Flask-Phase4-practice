from app import app, db  # Make sure to replace 'app' with the correct variable name if it's different
from models import User

def seed_data():
    # Sample user data with simple names
    users_data = [
        {'username': 'messi10', 'email': 'messi@example.com', 'password': 'messipass'},
        {'username': 'ronaldo7', 'email': 'ronaldo@example.com', 'password': 'ronaldopass'},
        {'username': 'neymar11', 'email': 'neymar@example.com', 'password': 'neymarpass'},
        {'username': 'modric10', 'email': 'modric@example.com', 'password': 'modricpass'},
        {'username': 'mbappe7', 'email': 'mbappe@example.com', 'password': 'mbappepass'},
    ]

    # Populate the database
    with app.app_context():
        for user_data in users_data:
            user = User(username=user_data['username'], email=user_data['email'])
            user.set_password(user_data['password'])
            db.session.add(user)

        # Commit the changes
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print('Database seeded successfully!')
