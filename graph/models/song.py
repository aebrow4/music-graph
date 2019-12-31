from neomodel import StructuredNode, UniqueIdProperty, StringProperty, Relationship


class Song(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    artists = Relationship(".artist.Artist", "PRODUCES")
    releases = Relationship(".release.Release", "CONTAINS")
    genre = Relationship(".genre.Genre", "CONTAINS")
    label = Relationship(".label.Label", "RELEASES")
