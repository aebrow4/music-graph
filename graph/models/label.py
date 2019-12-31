from neomodel import (
    StructuredNode,
    Relationship,
    UniqueIdProperty,
    StringProperty,
    DateProperty,
)


class Label(StructuredNode):
    uid = UniqueIdProperty()
    catalogue_number = StringProperty()
    date = DateProperty()
    artists = Relationship(".artist.Artist", "ASSOCIATES_WITH")
    songs = Relationship(".song.Song", "RELEASED_BY")
    releases = Relationship(".release.Release", "RELEASED_BY")
    genre = Relationship(".genre.Genre", "ASSOCIATES_WITH")
