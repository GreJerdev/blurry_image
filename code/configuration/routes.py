from flask import Flask
from api.controller.check_image import check_image



def init_routes(app:Flask):
    app.add_url_rule(
    "/check_image/<name>",  view_func=check_image, methods=["POST"] )
    app.add_url_rule(
    "/check_image/<name>",  view_func=check_image, methods=["PUT"] )