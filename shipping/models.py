from datetime import datetime
from shipping import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_number = db.Column(db.String(20), nullable=False)
    companyName = db.Column(db.String(80), nullable=False)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    zip_code = db.Column(db.String(20), nullable = False)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)

    packages = db.relationship('Package', backref='client', lazy=True)

    def __repr__(self):
        return f"Client('{self.fname}', '{self.lname}', '{self.phone_number}')"

class Receiver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable = False)
    lname = db.Column(db.String(80), nullable = False)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    
    packages = db.relationship('Package', backref='receiver', lazy=True)
    
    
    def __repr__(self):
        return f"Receiver('{self.fname}', '{self.lname}', '{self.phone_number}')"

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    weight = db.Column(db.String(5), nullable=False)
    dimension = db.Column(db.String(20), nullable=False)
    value = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    via = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sender_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('receiver.id'), nullable=False)

    def __repr__(self):
        return f"Package('{self.description}','{self.weight}', '{self.value}', '{self.price}')"