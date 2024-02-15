import json
from .models import Author
from .database import db
from .validate import validate_payload
from flask import Blueprint, request, jsonify


main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "Hello World"


@main.route("/authors", methods=["POST"])
def insert_author():
    if request.method == "POST":
        res = request.json
        keys = list(res.keys())

        if validate_payload(keys, "author"):
            return jsonify({"error": "invalid payload"})

    new_author = Author(name=res.get("name"), date_of_birth=res.get("date_of_birth"))
    db.session.add(new_author)
    db.session.commit()

    return jsonify(
        {"name": new_author.name, "date_of_birth:": new_author.date_of_birth}
    )
