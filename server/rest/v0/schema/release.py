from marshmallow import fields, Schema

from server.rest import ThinArtistSchema, ThinLabelSchema, ThinGenreSchema, ThinSongSchema


# PUT /release
class ReleaseRequestBodySchema(Schema):
    catalogue_num = fields.String(required=True)
    title = fields.String()
    release_date = fields.Date(required=True)

# Response for a single release
# GET, PUT, PATCH /release?foo=bar
class ReleaseResponseSchema(Schema):
    uid = fields.String(required=True)
    catalogue_num = fields.String(required=True)
    release_date = fields.Date(required=True)
    title = fields.String()
    artists = fields.List(fields.Nested(ThinArtistSchema))
    genres  = fields.List(fields.Nested(ThinGenreSchema))
    labels  = fields.List(fields.Nested(ThinLabelSchema))
    songs = fields.List(fields.Nested(ThinSongSchema))
