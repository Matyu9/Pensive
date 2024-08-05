from flask import request, jsonify
from cantinaUtils.verify_login import verify_login


def home_cogs(database):
    if request.method == "POST":
        verify_login(database)
        return jsonify(message="receive your data bb")
    else:
        return jsonify(message="Hello World!")
