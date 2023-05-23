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

@staticmethod
def save_meme(user_id: int, meme_id: int) -> None:
    save = Save(user_id=user_id, meme_id=meme_id)
    db.session.add(save)
    db.session.commit()
