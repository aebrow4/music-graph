from marshmallow import fields, Schema

from server.rest import ThinArtistSchema, ThinLabelSchema, ThinReleaseSchema, ThinSongSchema


# PUT /genre
class GenreRequestBodySchema(Schema):
    genre = fields.String()

# Response for a single genre
# GET, PUT, PATCH /genre?foo=bar
class GenreResponseSchema(Schema):
    uid = fields.UUID(required=True)
    genre = fields.String(required=True)
    artists  = fields.List(fields.Nested(ThinArtistSchema))
    labels  = fields.List(fields.Nested(ThinLabelSchema))
    releases = fields.List(fields.Nested(ThinReleaseSchema))
    songs = fields.List(fields.Nested(ThinSongSchema))
