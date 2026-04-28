import uuid
from backend.db import SessionLocal
from backend.models import APIKey


def create_api_key(username: str):
    db = SessionLocal()

    key = str(uuid.uuid4())

    api = APIKey(username=username, key=key, usage=0)

    db.add(api)
    db.commit()
    db.close()

    return key
