from datetime import datetime
from .models import Chambre


def get_available_rooms(rooms: list, check_in_date: str, check_out_date: str) -> list:
    available_rooms = []
    check_in_date_object = datetime.strptime(check_in_date, "%Y-%m-%d").date()
    check_out_date_object = datetime.strptime(check_out_date, "%Y-%m-%d").date()

    for room in rooms:
        if ~room_has_reservation(
            room,
            check_in_date_object,
            check_out_date_object,
        ):
            available_rooms.append(room)

    if available_rooms is None:
        return []

    return available_rooms


def room_has_reservation(room_to_check: Chambre, check_in_date, check_out_date) -> bool:
    for reservation in room_to_check.reservations:
        if is_the_same_dates(check_in_date, check_out_date, reservation):
            return True

        if check_in_date_inside_booking(check_in_date, check_out_date, reservation):
            return True

        if check_out_date_inside_booking(check_in_date, check_out_date, reservation):
            return True

        if check_out_date_inside_booking(
            check_in_date, check_out_date, reservation
        ) and check_out_date_inside_booking(check_in_date, check_out_date, reservation):
            return True

    return False


def is_the_same_dates(check_in_date, check_out_date, reservation_of_room):
    if (
        check_in_date == reservation_of_room.date_arrivee
        and check_out_date == reservation_of_room.date_depart
    ):
        return True

    return False


def check_in_date_inside_booking(check_in_date, check_out_date, reservation_of_room):
    if (
        check_in_date >= reservation_of_room.date_arrivee
        and check_out_date <= reservation_of_room.date_depart
    ):
        return True

    return False


def check_out_date_inside_booking(check_in_date, check_out_date, reservation_of_room):
    if (
        check_in_date <= reservation_of_room.date_arrivee
        and check_out_date >= reservation_of_room.date_depart
    ):
        return True

    return False
