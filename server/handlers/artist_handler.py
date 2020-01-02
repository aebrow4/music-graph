from flask import g

from server.rebar import rebar, registry
from rest.v0.schema.artist import ArtistResponseSchema
from rest.service.artist import create_artist, get_artists


def handle_create_artist():
    name = rebar.validated_body["name"]

    artist = create_artist(name)
    resp = ArtistResponseSchema().load(artist.to_dict())
    return resp

def handle_get_artists():
    artists = get_artists()
    return ArtistResponseSchema(many=True).load([a.to_dict() for a in artists])

def handle_update_artist(artist):
    # TODO
    # something like this
    some_release = Release.nodes.all()
    some_release.artists.connect(artist)
