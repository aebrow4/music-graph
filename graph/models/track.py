from neomodel import StructuredNode, UniqueIdProperty, StringProperty, Relationship


class Track(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    releases = Relationship(".release.Release", "RELEASES")
    genre = StringProperty()
