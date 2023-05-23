import os
from flask import render_template, redirect, url_for, flash, Response, Request
from flask_login import current_user, login_required
from app import db
from app.models import Meme, Save
from . import endpoint
from app import conf

admin_password = conf.ADMIN_SECRET

@endpoint.route("/meme/page/<int:page_num>", methods=["GET"])
def get_memes_page(page_num):
    skip = page_num * 10
    memes = Meme.query.order_by(Meme.created_at.desc()).offset(skip).limit(10)
    return render_template("memes_gallery.html", memes=memes)

@endpoint.route("/meme/<int:meme_id>", methods=["GET"])
def get_meme(meme_id):
    meme = Meme.query.filter_by(id=meme_id).first()
    return render_template("meme.html", meme=meme)

