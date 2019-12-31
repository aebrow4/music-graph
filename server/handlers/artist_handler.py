from flask import g

from server.rebar import rebar, registry
from server.rest.v0.schema.artist import ArtistResponseSchema
from graph.models.artist import Artist


def create_artist():
    name = rebar.validated_body["name"]

    artist = Artist(name=name).save()
    resp = ArtistResponseSchema().load(artist.to_dict())
    return resp

def get_artists():
    artists = Artist.nodes.all()
    return ArtistResponseSchema(many=True).load([a.to_dict() for a in artists])

def update_artist(artist):
    # TODO
    # something like this
    some_release = Release.nodes.all()
    some_release.artists.connect(artist)

def _wipe_artists():
    for node in Artist.nodes.all():
        node.delete()
