from flask import Blueprint
from src.controllers.controller import home, get_list

routes = Blueprint("routes", __name__)
routes.route("/", methods=["GET"])(home)
routes.route("/getlist", methods=["GET"])(get_list)
