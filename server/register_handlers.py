from server.handlers.hello_world import hello
from server.handlers.artist_handler import create_artist, get_artists


def register_handlers(app):
    @app.route("/hello", methods=["GET"])
    def _hello():
        return hello()

    @app.route("/artist", methods=["GET"])
    def _get_artists():
        return get_artists()

    @app.route("/artist", methods=["POST"])
    def _create_artist():
        return create_artist("bob2")
