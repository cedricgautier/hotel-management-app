# Available Rooms Checker

This module provides functions to check the availability of rooms based on reservation dates.

## Functions:

### `get_available_rooms(rooms: list, check_in_date: str, check_out_date: str) -> list`

- **Description:** Checks the availability of rooms for a given check-in and check-out dates.
- **Parameters:**
  - `rooms`: List of `Chambre` objects representing rooms.
  - `check_in_date`: String representing the check-in date in the format "%Y-%m-%d".
  - `check_out_date`: String representing the check-out date in the format "%Y-%m-%d".
- **Returns:** List of available `Chambre` objects.

### `room_has_reservation(room_to_check: Chambre, check_in_date, check_out_date) -> bool`

- **Description:** Checks if a room has a reservation overlapping with the specified check-in and check-out dates.
- **Parameters:**
  - `room_to_check`: A `Chambre` object representing the room to check for reservations.
  - `check_in_date`: Check-in date.
  - `check_out_date`: Check-out date.
- **Returns:** `True` if the room has a reservation during the specified dates, otherwise `False`.

### Helper Functions:

- `is_the_same_dates(check_in_date, check_out_date, reservation_of_room)`
- `check_in_date_inside_booking(check_in_date, check_out_date, reservation_of_room)`
- `check_out_date_inside_booking(check_in_date, check_out_date, reservation_of_room)`

These functions are helper functions used internally by `room_has_reservation` to check different scenarios of date overlaps with reservations.

## Usage:

```python
from datetime import datetime
from .models import Chambre
from .availability_checker import get_available_rooms

# Example usage:
check_in_date = "2024-02-20"
check_out_date = "2024-02-25"

# Retrieve rooms from the database
rooms = Chambre.query.all()

# Check available rooms
available_rooms = get_available_rooms(rooms, check_in_date, check_out_date)

if available_rooms:
    print("Available rooms:")
    for room in available_rooms:
        print(f"Room ID: {room.id}, Type: {room.type}, Number: {room.numero}")
else:
    print("No rooms available for the specified dates.")
```

## Notes:

- This module assumes the existence of a `Chambre` model representing rooms with reservations stored as a list within each room object.
- Ensure the database is properly configured and populated with reservation data before using these functions.
