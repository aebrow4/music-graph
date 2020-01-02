from marshmallow import fields, Schema

from rest import ThinArtistSchema, ThinLabelSchema, ThinReleaseSchema, ThinGenreSchema


# PUT /song
class SongRequestBodySchema(Schema):
    title = fields.String()

# Response for a single song
# GET, PUT, PATCH /song?foo=bar
class SongResponseSchema(Schema):
    uid = fields.UUID(required=True)
    title = fields.String(required=True)
    artists = fields.List(fields.Nested(ThinArtistSchema))
    genres  = fields.List(fields.Nested(ThinGenreSchema))
    labels  = fields.List(fields.Nested(ThinLabelSchema))
    releases = fields.List(fields.Nested(ThinReleaseSchema))
