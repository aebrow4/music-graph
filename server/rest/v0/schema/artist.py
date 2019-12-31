from marshmallow import fields, Schema
from server.rest import ThinGenreSchema, ThinLabelSchema, ThinReleaseSchema, ThinSongSchema


# PUT /artist
class ArtistRequestBodySchema(Schema):
    name = fields.String()

# Response for a single artist
# GET, PUT, PATCH /artist?foo=bar
class ArtistResponseSchema(Schema):
    uid = fields.String(required=True)
    name = fields.String(required=True)
    genres  = fields.List(fields.Nested(ThinGenreSchema))
    labels  = fields.List(fields.Nested(ThinLabelSchema))
    releases = fields.List(fields.Nested(ThinReleaseSchema))
    songs = fields.List(fields.Nested(ThinSongSchema))
