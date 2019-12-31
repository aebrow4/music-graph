from marshmallow import fields, Schema


class ThinArtistSchema(Schema):
    uid = fields.String(required=True)
    name = fields.String(required=True)

class ThinGenreSchema(Schema):
    uid = fields.String(required=True)
    genre = fields.String(required=True)

class ThinLabelSchema(Schema):
    uid = fields.String(required=True)
    name = fields.String(required=True)

class ThinReleaseSchema(Schema):
    uid = fields.String(required=True)
    catalogue_num = fields.String(required=True)

class ThinSongSchema(Schema):
    uid = fields.String(required=True)
    title = fields.String(required=True)

