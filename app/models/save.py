from .user import User
from .meme import Meme
from app import db


class Save(db.Model):
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(User.id, ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    meme_id = db.Column(
        db.Integer,
        db.ForeignKey(Meme.id, ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
