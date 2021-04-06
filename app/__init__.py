from flask import Flask


def create_app():
    app = Flask(__name__)

    from .views.timeline_view import bp_timeline
    app.register_blueprint(bp_timeline)

    return app
