from marshmallow import fields, Schema

from rest import ThinArtistSchema, ThinGenreSchema, ThinReleaseSchema, ThinSongSchema


# PUT /label
class LabelRequestBodySchema(Schema):
    name = fields.String()

# Response for a single label
# GET, PUT, PATCH /label?foo=bar
class LabelResponseSchema(Schema):
    uid = fields.UUID(required=True)
    name = fields.String(required=True)
    artists  = fields.List(fields.Nested(ThinArtistSchema))
    genres  = fields.List(fields.Nested(ThinGenreSchema))
    releases = fields.List(fields.Nested(ThinReleaseSchema))
    songs = fields.List(fields.Nested(ThinSongSchema))
