from .database import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, default=nom + "@test.com")
    reservations = db.relationship("Reservation", backref="client", lazy=True)


class Chambre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), unique=True, nullable=False, autoincrement=True)
    type = db.Column(db.String(50), default="Standard")
    prix = db.Column(db.Float, default=75)
    reservations = db.relationship("Reservation", backref="chambre", lazy=True)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_client = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    id_chambre = db.Column(db.Integer, db.ForeignKey("chambre.id"), nullable=False)
    date_arrivee = db.Column(db.Date, nullable=False)
    date_depart = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50))
