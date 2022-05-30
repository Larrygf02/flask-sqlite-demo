
def get_fields(payload, fields):
    data = []
    for field in fields:
        data.append(payload[field])
    return data

def valid_payload(payload, fields):
    for field in fields:
        if field not in payload:
            raise Exception("Invalid payload")
    return True

def valid_update(payload, fields):
    for key in payload.keys():
        if key not in fields:
            raise Exception(f"Invalid item {key}")
    return True