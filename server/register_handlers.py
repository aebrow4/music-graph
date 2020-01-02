from server.rebar import registry
from server.handlers.hello_world import hello
from server.handlers.artist_handler import handle_create_artist, handle_get_artists
from server.handlers.release_handler import handle_create_release, handle_get_releases, handle_update_release
from rest.v0.schema.artist import ArtistRequestBodySchema, ArtistResponseSchema
from rest.v0.schema.release import ReleasePutSchema, ReleasePatchSchema, ReleaseResponseSchema

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
        return handle_get_artists()

    @registry.handles(
          rule="/artist",
          method="PUT",
          request_body_schema=ArtistRequestBodySchema,
          response_body_schema=ArtistResponseSchema)
    def _create_artist():
        return handle_create_artist()

    # Releases
    @registry.handles(
            rule="/release",
            method="GET",
            response_body_schema=ReleaseResponseSchema(many=True))
    def _get_releases():
        return handle_get_releases()

    @registry.handles(
          rule="/release",
          method="PUT",
          request_body_schema=ReleasePutSchema,
          response_body_schema=ReleaseResponseSchema)
    def _create_release():
        return handle_create_release()

    @registry.handles(
          rule="/release",
          method="PATCH",
          # request_body_schema=ReleasePatchSchema,
          response_body_schema=ReleaseResponseSchema)
    def _update_release():
        return handle_update_release('bd0866f867ad4d5ebb340a58e3afacd6')
