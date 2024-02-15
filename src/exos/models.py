from .database import db
from datetime import datetime, timezone


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    reservations = db.relationship("Reservation", backref="client", lazy=True)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50), unique=True)
    type = db.Column(db.String(50))
    price = db.Column(db.Integer)
    reservations = db.relationship("Reservation", backref="room", lazy=True)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    check_in_date = db.Column(db.DateTime, default=datetime.now())
    check_out_date = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String(50))
