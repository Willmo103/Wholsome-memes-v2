from app import db
from sqlalchemy import TIMESTAMP

class Meme(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    url = db.Column(db.String, nullable=False)
    created_at = db.Column(TIMESTAMP(timezone = True), nullable=False, server_default=db.func.now())
