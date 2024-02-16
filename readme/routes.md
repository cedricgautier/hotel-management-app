# API Documentation

This document provides an overview of the routes available in the main Blueprint of the application.

## Index

- **Route:** `/`
- **Method:** GET
- **Description:** A simple greeting message.

## Insert Client

- **Route:** `/api/clients`
- **Method:** POST
- **Description:** Inserts a new client into the database.
- **Request Body:**
  - `nom` (string): Name of the client.
  - `email` (string): Email of the client.

## Get or Create Chambre

- **Route:** `/api/chambres`
- **Methods:** GET, POST
- **Description:** Retrieves all rooms or creates a new room.

### GET Request

- **Description:** Retrieves all rooms from the database.
- **Response:** JSON object containing details of all rooms.

### POST Request

- **Description:** Creates a new room and adds it to the database.
- **Request Body:**
  - `numero` (string): Room number.
  - `type` (string): Type of room.
  - `prix` (float): Price of the room.
- **Response:** Success message if the room is successfully added.

## Search Available Rooms

- **Route:** `/api/chambres/disponibles`
- **Method:** GET
- **Description:** Searches for available rooms based on provided dates.
- **Request Body:**
  - `date_arrivee` (string): Arrival date.
  - `date_depart` (string): Departure date.
- **Response:** JSON object containing details of available rooms.

## Create 100 Standard Rooms

- **Route:** `/api/chambres/add-batch`
- **Method:** GET
- **Description:** Creates 100 standard rooms and adds them to the database.
- **Response:** Success message if the rooms are successfully added.

## Delete All Rooms

- **Route:** `/api/chambres/delete-all`
- **Method:** DELETE
- **Description:** Deletes all rooms from the database.
- **Response:** Success message if all rooms are successfully deleted.

## Modify or Delete Chambre

- **Route:** `/api/chambres/<int:id>`
- **Methods:** PUT, DELETE
- **Description:** Modifies or deletes a room based on provided ID.

### PUT Request

- **Description:** Modifies details of a room.
- **Request Body:** JSON object containing updated room details.
- **Response:** Success message if the room is successfully updated.

### DELETE Request

- **Description:** Deletes a room.
- **Response:** Success message if the room is successfully deleted.

## Get or Create Reservations

- **Route:** `/api/reservations`
- **Method:** POST
- **Description:** Creates a new reservation for a client.
- **Request Body:**
  - `id_client` (int): ID of the client.
  - `date_arrivee` (string): Arrival date.
  - `date_depart` (string): Departure date.
  - `statut` (string): Status of the reservation.
- **Response:** Success message if the reservation is successfully created.

## Delete Reservation

- **Route:** `/api/reservations/<int:id>`
- **Methods:** DELETE
- **Description:** Deletes a reservation based on provided ID.
- **Response:** Success message if the reservation is successfully deleted.
