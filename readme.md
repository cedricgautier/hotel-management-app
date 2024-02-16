# Hotel Management API

A comprehensive hotel management system to streamline operations and manage reservations efficiently.

## Table of Contents

- [Hotel Management System](#hotel-management-system)

  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Usage](#usage)

## Description

The Hotel Management API is designed to automate various tasks involved in managing a hotel, including client management, room reservations, and room management.

## Features

- Client management: Add clients.
- Rooms management: Add, update, and delete room details.
- Reservation management: Create and cancel room reservations.
- Batch operations: Ability to create multiple standard rooms in batches.
- Availability checker: Check the availability of rooms based on specified dates.

## Usage

To use the Hotel Management System, follow these steps:

1. Start the application by running `docker compose up --build` from the root of the project.

There might be issues, you might need to add a env file and add the needed variables. (env.sample file to find which vars to add)

2. Check if the password is generated when you up the db container.

- if yes : you'll need to follow these steps :

  - Find the secret that the database generated in the logs of the db container
  - Exectute the running db container to check if the credentials are correct with : "mysql -p" (add your password when asked)
  - Go to your env file and complete the DBURI with the password generated
    (You can change the docker file if needed, it starts with a debug mode on)

    You are free to modify the docker files to your liking to make the setup to work

3. Run flask commands from the project folder on the container (app/src/tp-ced):
   - `flask db init`
   - `flask db migrate`
   - `flask db upgrade`
