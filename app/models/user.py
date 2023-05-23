from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(120), unique=True, nullable=True)
    password: str = db.Column(db.String(120), nullable=False)
    created_at: str = db.Column(
        db.TIMESTAMP(timezone=True), nullable=False, server_default=db.func.now()
    )

    def set_password(self, password) -> None:
        self.password = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)

    @staticmethod
    def get_user(user_id: int):
        user: User = User.query.filter_by(id=user_id).first()
        if user is None:
            raise Exception("User not found")
        return user
