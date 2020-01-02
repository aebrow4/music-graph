from flask import g

from server.rebar import rebar, registry
from rest.v0.schema.artist import ArtistResponseSchema
from rest.service.artist import create_artist, get_artists, update_artist


def handle_create_artist():
    name = rebar.validated_body["name"]

    artist = create_artist(name)
    resp = ArtistResponseSchema().load(artist.to_dict())
    return resp

def handle_get_artists():
    artists = get_artists()
    return ArtistResponseSchema(many=True).load([a.to_dict() for a in artists])

def handle_update_artist():
    uid = rebar.validated_body.get("uid")
    updates = {
            'name': rebar.validated_body.get('name'),
            'genres': rebar.validated_body.get('genres', []),
            'labels': rebar.validated_body.get('labels', []),
            'releases': rebar.validated_body.get('releases', []),
            'songs': rebar.validated_body.get('songs', []),
        }

    updated = update_artist(uid, updates)
           
    return ArtistResponseSchema().load(updated.to_dict())
