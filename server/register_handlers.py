from server.rebar import registry
from server.handlers.hello_world import hello
from server.handlers.artist_handler import create_artist, get_artists
from server.handlers.release_handler import create_release, get_releases
from server.rest.v0.schema.artist import ArtistRequestBodySchema, ArtistResponseSchema
from server.rest.v0.schema.release import ReleaseRequestBodySchema, ReleaseResponseSchema

def register_handlers():

    @registry.handles(
            rule="/hello",
            method="GET")
    def _hello():
        return hello()

    # Artists
    @registry.handles(
            rule="/artist",
            method="GET",
            response_body_schema=ArtistResponseSchema(many=True))
    def _get_artists():
        return get_artists()

    @registry.handles(
          rule="/artist",
          method="PUT",
          request_body_schema=ArtistRequestBodySchema,
          response_body_schema=ArtistResponseSchema)
    def _create_artist():
        return create_artist()

    # Releases
    @registry.handles(
            rule="/release",
            method="GET",
            response_body_schema=ReleaseResponseSchema(many=True))
    def _get_releases():
        return get_releases()

    @registry.handles(
          rule="/release",
          method="PUT",
          request_body_schema=ReleaseRequestBodySchema,
          response_body_schema=ReleaseResponseSchema)
    def _create_release():
        return create_release()
