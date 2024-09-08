from datetime import datetime
import uuid

def generate_session_id():
    # Current time with microseconds to ensure uniqueness as much as possible
    current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
    # Generate a random UUID
    unique_id = str(uuid.uuid4())
    # Combine them
    session_id = f"{current_time}"
    return session_id