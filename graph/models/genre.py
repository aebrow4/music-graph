from neomodel import (
    StructuredNode,
    Relationship,
    UniqueIdProperty,
    StringProperty,
    DateProperty,
)


class Genre(StructuredNode):
    uid = UniqueIdProperty()
    artists = Relationship(".artist.Artist", "ASSOCIATES_WITH")
    songs = Relationship(".song.Song", "CONTAINED_BY")
    releases = Relationship(".genre.Genre", "ASSOCIATES_WITH")
    label = Relationship(".label.Label", "ASSOCIATES_WITH")

