from flask import Flask, Blueprint
from app.controllers import user_controller

bp = Blueprint('users', __name__, url_prefix="/users")

bp.post("")(user_controller.create_user)