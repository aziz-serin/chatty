from flask import Blueprint, send_from_directory
from . import BASE_PATH

home = Blueprint('home', "chatty")

@home.route("/")
def context_endpoint():
    return send_from_directory(BASE_PATH, "index.html")
