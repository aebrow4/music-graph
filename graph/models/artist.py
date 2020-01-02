from neomodel import StructuredNode, UniqueIdProperty, StringProperty, Relationship

from graph.models.base_model import BaseModel


class Artist(BaseModel, StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    releases = Relationship(".release.Release", "PRODUCED_BY")
    songs = Relationship(".song.Song", "PRODUCES")
    genres = Relationship(".genre.Genre", "ASSOCIATES_WITH")
    labels = Relationship(".label.Label", "ASSOCIATES_WITH")
