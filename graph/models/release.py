from neomodel import (
    StructuredNode,
    Relationship,
    UniqueIdProperty,
    StringProperty,
    DateProperty,
)

from graph.models.base_model import BaseModel


class Release(BaseModel, StructuredNode):
    uid = UniqueIdProperty()
    catalogue_num = StringProperty(required=True)
    release_date = DateProperty()
    title = StringProperty()
    artists = Relationship(".artist.Artist", "PRODUCES")
    genre = Relationship(".genre.Genre", "ASSOCIATES_WITH")
    label = Relationship(".label.Label", "RELEASES")
    songs = Relationship(".song.Song", "CONTAINED_BY")
