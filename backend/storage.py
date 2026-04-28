from backend.db import SessionLocal
from sqlalchemy import text


def save_project(topic, blog, keywords):
    db = SessionLocal()

    try:
        db.execute(
            text("INSERT INTO projects (topic, blog, keywords) VALUES (:topic, :blog, :keywords)"),
            {"topic": topic, "blog": blog, "keywords": keywords}
        )
        db.commit()
    finally:
        db.close()


def get_projects():
    db = SessionLocal()

    try:
        result = db.execute(
            text("SELECT * FROM projects ORDER BY id DESC")
        )

        rows = result.fetchall()

        return [dict(row._mapping) for row in rows]

    finally:
        db.close()
