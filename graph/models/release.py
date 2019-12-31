from neomodel import (
    StructuredNode,
    Relationship,
    UniqueIdProperty,
    StringProperty,
    DateProperty,
)


class Release(StructuredNode):
    uid = UniqueIdProperty()
    catalogue_number = StringProperty()
    label = StringProperty()
    artists = Relationship(".artist.Artist", "RELEASES")
    tracks = Relationship(".track.Track", "CONTAINS")
    date = DateProperty()
