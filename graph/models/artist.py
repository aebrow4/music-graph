from neomodel import StructuredNode, UniqueIdProperty, StringProperty, Relationship


class Artist(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    releases = Relationship(".release.Release", "RELEASES")
