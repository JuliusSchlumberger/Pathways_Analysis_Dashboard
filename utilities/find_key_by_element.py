def find_key_by_value(value, dictionary):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Return None if the value is not found
