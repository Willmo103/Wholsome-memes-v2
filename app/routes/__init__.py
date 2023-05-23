from flask import Blueprint

endpoint = Blueprint("routes", __name__)

from .auth import (
    login as login,
    logout as logout,
    register as register,
)

from .meme import (
    get_memes_page as get_memes_page,
    get_meme as get_meme,
)
