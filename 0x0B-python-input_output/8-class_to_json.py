def class_to_json(obj):
    """
    Serialize an object into a dictionary with simple data structures 
    for JSON serialization.

    Parameters:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object.
    """
    if not hasattr(obj, '__dict__'):
        return None

    serialized = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized[key] = value

    return serialized
