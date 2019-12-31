from graph.models.artist import Artist
from graph.models.release import Release
from graph.models.track import Track


def create_artist(artist):
    for node in Artist.nodes.all():
        node.delete()
    for node in Release.nodes.all():
        node.delete()
    for node in Track.nodes.all():
        node.delete()

    t = Track(name="club bangeer", genre="techno").save()
    r1 = Release(catalogue_number="REL-001").save()
    a = Artist(name=artist).save()
    r1.artists.connect(a)
    r1.tracks.connect(t)
    # This won't print the artist's releases, but they are there
    print(f"artists: {Artist.nodes.all()} ")
    return "ok"


