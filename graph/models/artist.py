from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo


class Artist(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)


twisted_sister = Artist(name="Twisted Sister")
metallica = Artist(name="Metallica")
