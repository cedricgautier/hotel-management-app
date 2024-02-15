def validate_payload(payload_keys, model):
    keys = []
    required_keys = []

    if model == "author":
        keys = ["name", "date_of_birth"]
        required_keys = ["name"]
    elif model == "book":
        keys = ["title", "publication_date", "genre", "author_id"]
        required_keys = ["title"]
    elif model == "user":
        keys = ["name", "email", "books"]
        required_keys = ["name", "email"]
    elif model == "loan":
        keys = ["user_id", "book_id", "loaned_date", "return_date"]

    for payload_key in payload_keys:
        if payload_key not in keys:
            return True

    for req_key in required_keys:
        if req_key not in payload_keys:
            return True

    return False
