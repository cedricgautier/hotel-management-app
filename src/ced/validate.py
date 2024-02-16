from .constants import (
    client_string,
    room_string,
    nom_string,
    email_string,
    client_reservations_string,
    numero_string,
    type_string,
    prix_string,
)


def validate_payload_post(payload_keys, model):
    keys = []
    required_keys = []

    if model == client_string:
        keys = [nom_string, email_string, client_reservations_string]
        required_keys = [nom_string]

    elif model == room_string:
        keys = [numero_string, type_string, prix_string]
        required_keys = [numero_string]

    for payload_key in payload_keys:
        if payload_key not in keys:
            return True

    for req_key in required_keys:
        if req_key not in payload_keys:
            return True

    return False
