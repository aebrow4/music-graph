from marshmallow import fields, Schema

class ArtistRequestBodySchema(Schema):
    name = fields.String()
