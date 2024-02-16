import random, logging
from .chambres import get_available_rooms
from .models import Client, Chambre, Reservation
from .database import db
from .validate import validate_payload_post
from .constants import *
from flask import Blueprint, request, jsonify


main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "Hello World"


@main.route("/api/clients", methods=["POST"])
def insert_client():
    if request.method == post_string:
        res = request.json
        keys = list(res.keys())

        if validate_payload_post(keys, client_string):
            return jsonify(error_payload)

    new_client = Client(nom=res.get(nom_string), email=res.get(email_string))
    db.session.add(new_client)
    db.session.commit()

    return jsonify(
        {
            nom_string: new_client.nom,
            email_string: new_client.email,
        }
    )


@main.route("/api/chambres", methods=["GET", "POST"])
def get_or_create_chambre():
    response = {}
    if request.method == get_string:
        rooms = Chambre.query.all()

        if rooms is not None:
            for room in rooms:
                room_details = {
                    numero_string: room.numero,
                    type_string: room.type,
                    prix_string: room.prix,
                    numero_string: room.numero,
                }

                response[room.id] = room_details

            try:
                return jsonify({all_rooms_string: response})
            except Exception as e:
                return jsonify(error_get_payload)
        return jsonify(no_rooms_available_string)

    if request.method == post_string:
        res = request.json
        keys = list(res.keys())

        if validate_payload_post(keys, room_string):
            return jsonify(error_payload)

        new_room = Chambre(
            numero=res.get(numero_string),
            type=res.get(type_string),
            prix=res.get(prix_string),
        )
        db.session.add(new_room)
        db.session.commit()

        return jsonify(
            {success_string: True, message_string: success_chambre_add_string}
        )


@main.route("/api/chambres/disponibles", methods=["GET"])
def search_available_rooms():
    if request.method == get_string:
        res = request.json
        date_arrivee = res.get(date_arrivee_string)
        date_depart = res.get(date_depart_string)
        rooms = Chambre.query.all()
        available_rooms = get_available_rooms(rooms, date_arrivee, date_depart)

        if available_rooms is None:
            return jsonify(no_rooms_available_string)

        return jsonify(
            chambres=[
                {
                    id_string: room.id,
                    type_string: room.type,
                    numero_string: room.numero,
                    client_reservations_string: room.reservations,
                }
                for room in available_rooms
            ]
        )


@main.route("/api/chambres/add-batch", methods=["POST"])
def create_100_standard_rooms():
    if request.method == post_string:
        rooms = Chambre.query.all()
        for x in range(100):
            try:
                new_room = Chambre(numero=str(len(rooms) + x))
                db.session.add(new_room)
                db.session.commit()

            except Exception:
                return jsonify(error_add_payload)

        return jsonify(
            {
                success_string: True,
                message_string: success_chambre_add_string + "100 rooms",
            }
        )


@main.route("/api/chambres/delete-all", methods=["DELETE"])
def delete_all_rooms():
    if request.method == delete_string:
        try:
            db.session.query(Chambre).delete()
            db.session.commit()

            return jsonify(
                {
                    success_string: True,
                    message_string: success_all_chambres_delete_string,
                }
            )
        except Exception:
            return jsonify(error_delete_all_payload)


@main.route("/api/chambres/<int:id>", methods=["PUT", "DELETE"])
def modify_delete_chambre(id):
    if request.method == put_string:
        res = request.json

        room = Chambre.query.get_or_404(id)
        if res.get(type_string) is not None:
            room.type = res.get(type_string)

        if res.get(prix_string) is not None:
            room.prix = res.get(prix_string)

        if res.get(numero_string) is not None:
            room.numero = res.get(numero_string)

        try:
            db.session.commit()
            return jsonify(
                {success_string: True, message_string: success_chambre_maj_string}
            )

        except Exception:
            return jsonify({error_modify_payload})

    if request.method == delete_string:
        room_from_id = Chambre.query.get_or_404(id)
        db.session.delete(room_from_id)
        db.session.commit()

        return jsonify(
            {success_string: True, message_string: success_chambre_delete_string}
        )


@main.route("/api/reservations", methods=["POST"])
def get_or_create_reservations():
    if request.method == post_string:
        res = request.json
        date_arrivee = res.get(date_arrivee_string)
        date_depart = res.get(date_depart_string)

        rooms = Chambre.query.all()
        if rooms is None:
            return jsonify({response_string: no_rooms_available_string})

        available_rooms = get_available_rooms(rooms, date_arrivee, date_depart)
        if len(available_rooms) is 0:
            return jsonify({response_string: no_rooms_available_string})

        free_room = random.choice(available_rooms)

        new_reservation = Reservation(
            id_client=res.get(id_client_string),
            id_chambre=free_room.id,
            date_arrivee=date_arrivee,
            date_depart=date_depart,
            statut=res.get(statut_string),
        )

        db.session.add(new_reservation)

        try:
            db.session.commit()
            return jsonify(
                {
                    success_string: True,
                    message_string: success_reservation_add_string,
                }
            )
        except Exception:
            return jsonify({error_add_payload})


@main.route("/api/reservations/<int:id>", methods=["PUT", "DELETE"])
def delete_reservation(id):
    if request.method == delete_string:
        reservation = Reservation.query.get_or_404(id)
        db.session.delete(reservation)
        db.session.commit()

        return jsonify(
            {success_string: True, message_string: success_chambre_delete_string}
        )
