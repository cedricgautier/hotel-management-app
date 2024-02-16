# Payload Validation Function

This function is used to validate the payload keys sent in a POST request against the expected keys for a particular model.

## Function: `validate_payload_post(payload_keys, model)`

### Parameters:

- `payload_keys`: List of keys present in the payload of the POST request.
- `model`: String indicating the model for which the payload validation is being performed.

### Return Value:

- `True`: If the payload keys are invalid or incomplete.
- `False`: If the payload keys are valid.

### Models and Expected Keys:

- **Client Model (`client_string`):**

  - Expected Keys: `nom`, `email`, `client_reservations`
  - Required Keys: `nom`

- **Room Model (`room_string`):**
  - Expected Keys: `numero`, `type`, `prix`
  - Required Keys: `numero`

### Usage:

```python
# Example usage:
payload_keys = ["nom", "email"]
model = "client_string"

if validate_payload_post(payload_keys, model):
    # Handle invalid payload
    print("Invalid payload keys or incomplete payload.")
else:
    # Proceed with further processing
    print("Payload validation successful.")
```

### Notes:

- This function ensures that the payload contains all the required keys for a particular model and none of the unexpected keys.
- It returns `True` if the payload is invalid or incomplete, otherwise `False`.
