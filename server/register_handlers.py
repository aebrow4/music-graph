from server.handlers.hello_world import hello


def register_handlers(app):
    @app.route("/hello", methods=["GET"])
    def _hello():
        return hello()
