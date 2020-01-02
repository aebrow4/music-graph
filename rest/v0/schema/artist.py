from marshmallow import fields, Schema
from rest import ThinGenreSchema, ThinLabelSchema, ThinReleaseSchema, ThinSongSchema


# PUT /artist
class ArtistPutSchema(Schema):
    name = fields.String()

class ArtistPatchSchema(Schema):
    uid = fields.String(required=True)
    name = fields.String()
    releases = fields.List(fields.String())
    genres  = fields.List(fields.String())
    labels  = fields.List(fields.String())
    songs = fields.List(fields.String())

# Response for a single artist
# GET, PUT, PATCH /artist?foo=bar
class ArtistResponseSchema(Schema):
    uid = fields.String(required=True)
    name = fields.String(required=True)
    genres  = fields.List(fields.Nested(ThinGenreSchema))
    labels  = fields.List(fields.Nested(ThinLabelSchema))
    releases = fields.List(fields.Nested(ThinReleaseSchema))
    songs = fields.List(fields.Nested(ThinSongSchema))
