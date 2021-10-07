import connexion

from app import extensions


def create_app():
    # Setup connexion
    connexion_app = connexion.FlaskApp(__name__)
    connexion_app.add_api('api.yaml')
    flask_app = connexion_app.app

    # Flask setup
    extensions.init_app(flask_app)

    return flask_app
