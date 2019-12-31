from server.rebar import registry
from server.handlers.hello_world import hello
from server.handlers.artist_handler import create_artist, get_artists
from server.rest.v0.schema.artist import ArtistRequestBodySchema


def register_handlers():

    @registry.handles(
            rule="/hello",
            method="GET")
    def _hello():
        return hello()

    @registry.handles(
            rule="/artist",
            method="GET")
    def _get_artists():
        return get_artists()

    @registry.handles(
            rule="/artist",
            method="POST",
            request_body_schema=ArtistRequestBodySchema)
    def _create_artist():
        return create_artist()
