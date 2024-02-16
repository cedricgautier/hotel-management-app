# Documentation

This document provides an overview of all routes available in the application.

## Index

- **Route:** `/`
- **Method:** GET
- **Description:** Returns a simple greeting message.

## Insert Client

- **Route:** `/api/clients`
- **Method:** POST
- **Description:** Inserts a new client into the database.
- **Parameters:**
  - `nom` (string): Name of the client.
  - `email` (string): Email of the client.

## Get or Create Chambre

- **Route:** `/api/chambres`
- **Methods:** GET, POST
- **Description:** Retrieves all rooms or creates a new room.
- **GET Parameters:** None
- **POST Parameters:**
  - `numero` (string): Room number.
  - `type` (string): Type of room.
  - `prix` (float): Price of the room.

## Search Available Rooms

- **Route:** `/api/chambres/disponibles`
- **Method:** GET
- **Description:** Searches for available rooms based on provided dates.
- **Parameters:**
  - `date_arrivee` (string): Arrival date.
  - `date_depart` (string): Departure date.

## Create 100 Standard Rooms

- **Route:** `/api/chambres/add-batch`
- **Method:** POST
- **Description:** Creates 100 standard rooms.
- **Parameters:** None

## Delete All Rooms

- **Route:** `/api/chambres/delete-all`
- **Method:** DELETE
- **Description:** Deletes all rooms from the database.
- **Parameters:** None

## Modify or Delete Chambre

- **Route:** `/api/chambres/<int:id>`
- **Methods:** PUT, DELETE
- **Description:** Modifies or deletes a room based on provided ID.
- **PUT Parameters:**
  - `numero` (string): Room number.
  - `type` (string): Type of room.
  - `prix` (float): Price of the room.

## Get or Create Reservations

- **Route:** `/api/reservations`
- **Method:** POST
- **Description:** Inserts a new reservation into the database.
- **Parameters:**
  - `room_id` (int): ID of the room.
  - `client_id` (int): ID of the client.
  - `date_debut` (string): Start date of reservation.
  - `date_fin` (string): End date of reservation.

## Delete Reservation

- **Route:** `/api/reservations/<int:id>`
- **Methods:** DELETE
- **Description:** Deletes a reservation based on provided ID.
- **Parameters:** None
